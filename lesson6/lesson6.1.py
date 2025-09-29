#Сделать функцию которая определит роль студентов для будущей жизни
#Если ОРТ - 110 + он/она поступает в университет
#Если ОРТ от 80 - 109 поступает в колледж
#Если меньше 80 - то парни уходят на стройку, а девушки официантами

univer = []
kollege = []
construction = []
waiter = []




students = [
    {'name': 'SOFA', 'ORT': 110, 'male': 'f'},
    {'name': 'ALEX', 'ORT': 98, 'male': 'm'},
    {'name': 'LINA', 'ORT': 120, 'male': 'f'},
    {'name': 'TIMUR', 'ORT': 75, 'male': 'm'},
    {'name': 'DIANA', 'ORT': 13, 'male': 'f'},
    {'name': 'ERLAN', 'ORT': 88, 'male': 'm'},
    {'name': 'NURA', 'ORT': 147, 'male': 'f'},
    {'name': 'ALI', 'ORT': 52, 'male': 'm'},
    {'name': 'ZARA', 'ORT': 123, 'male': 'f'},
    {'name': 'OMAR', 'ORT': 101, 'male': 'm'},
    {'name': 'JANA', 'ORT': 111, 'male': 'f'},
    {'name': 'RUSLAN', 'ORT': 67, 'male': 'm'},
    {'name': 'MIRA', 'ORT': 89, 'male': 'f'},
    {'name': 'NURIS', 'ORT': 144, 'male': 'm'},
    {'name': 'LANA', 'ORT': 130, 'male': 'f'},
    {'name': 'DASTAN', 'ORT': 76, 'male': 'm'},
    {'name': 'AYNA', 'ORT': 93, 'male': 'f'},
    {'name': 'BAKT', 'ORT': 105, 'male': 'm'},
    {'name': 'ELINA', 'ORT': 114, 'male': 'f'},
    {'name': 'SAMAT', 'ORT': 83, 'male': 'm'},
    {'name': 'NINA', 'ORT': 134, 'male': 'f'},
    {'name': 'ASLAN', 'ORT': 60, 'male': 'm'},
    {'name': 'GULYA', 'ORT': 99, 'male': 'f'},
    {'name': 'ISLAM', 'ORT': 71, 'male': 'm'},
    {'name': 'RAISA', 'ORT': 149, 'male': 'f'},
    {'name': 'ARSLAN', 'ORT': 41, 'male': 'm'},
    {'name': 'SARA', 'ORT': 126, 'male': 'f'},
    {'name': 'TALGAT', 'ORT': 87, 'male': 'm'},
    {'name': 'AINURA', 'ORT': 13, 'male': 'f'},
    {'name': 'YERLAN', 'ORT': 53, 'male': 'm'},
    {'name': 'ALINA', 'ORT': 11, 'male': 'f'},
    {'name': 'AZAMAT', 'ORT': 109, 'male': 'm'}
]

def all_abit(lst):
    for i in lst:
        for k, v in i.items():
            return(f"{k}-{v}")
all_abit(lst=students)

def selection(lst, univer:list, kollege:list, construction:list, waiter:list):
    for i in lst:
        if i['ORT'] >= 110:
            univer.append(i)
        elif i['ORT'] >= 80 and i['ORT']<=109:
            kollege.append(i)
        elif i['ORT'] < 80 and i['male'] == 'm':
            construction.append(i)
        elif i['ORT'] < 80 and i ['male'] == 'f':
            waiter.append(i)

selection(lst=students, univer=univer, kollege=kollege, construction=construction, waiter=waiter)
#print(f'В Универ - {univer}')
print(f'Универ {[i['name'] for i in univer], [i['ORT'] for i in univer]}')
print('-'*20)
#print(f'В коллдеж - {kollege}')
print(f'Колледж {[i['name'] for i in kollege], [i['ORT'] for i in kollege]}')
print('-'*20)
#print(f'На стройку - {construction}')
print(f'Стройка {[i['name'] for i in construction], [i['ORT'] for i in construction]}')
print('-'*20)
#print(f'В Кафе - {waiter}')
print(f'Кафе {[i['name'] for i in waiter], [i['ORT'] for i in waiter]}')