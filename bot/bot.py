import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


API_TOKEN = '8484957268:AAHqjQysH2QFQlGTPhPVnkeb5yA0tfMc6D8'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Память для задач
user_tasks = {}

# Кнопки меню
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Добавить задачу')],
        [KeyboardButton(text='Мои задачи')],
        [KeyboardButton(text='Очистить задачи')]
    ],
    resize_keyboard=True
)

# start 
@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer('Привет, я твой новый бот!', reply_markup=keyboard)

# Программируем кнопку "Добавить задачу"
@dp.message(lambda msg: msg.text == 'Добавить задачу')
async def ask_task(message: types.Message):
    await message.answer('Напиши, что хочешь сделать на сегодня!')

# Мои задачи
@dp.message(lambda msg: msg.text == 'Мои задачи')
async def show_tasks(message: types.Message):
    user_id = message.from_user.id
    tasks = user_tasks.get(user_id, [])

    if not tasks:
        await message.answer('У вас нет задач')
        return
    
    text = "Ваши задачи:\n\n"
    for i, task in enumerate(tasks, 1):
        text += f'{i}. {task}\n'
    
    await message.answer(text)

# Удаление задач
@dp.message(lambda msg: msg.text == 'Очистить задачи')
async def clear_tasks(message: types.Message):
    user_id = message.from_user.id
    user_tasks[user_id] = []
    await message.answer('Все задачи удалены!')

# Сохранение задачи - должен быть ПОСЛЕ всех обработчиков кнопок
@dp.message()
async def save_task(message: types.Message):
    text = message.text

    # Проверяем, не является ли сообщение командой или кнопкой меню
    if text.startswith('/') or text in ['Добавить задачу', 'Мои задачи', "Очистить задачи"]:
        return
    
    user_id = message.from_user.id
    if user_id not in user_tasks:
        user_tasks[user_id] = []

    user_tasks[user_id].append(text)
    await message.answer(f'Задача была успешно добавлена:\n{text}')

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())