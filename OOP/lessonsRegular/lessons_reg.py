import re

# Указываем полный путь к файлу
file_path = r"C:\Users\kingr\Desktop\iuca1st_course\OOP\lessonsRegular\mockdata.txt"

with open(file_path, "r", encoding='utf-8') as f:
    text = f.read()

# Регулярное выражение для почты
emails = re.findall(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', text)

emails_list = list(emails)

#Регулярные выражения цвета
colors = re.findall(r'#(?:[0-9a-fA-F]{6})', text)
print(colors)

"""
Статья по регулярным выражениям на Habr:

 TODO  https://habr.com/ru/articles/349860/

Этот код извлекает email-адреса из файла с помощью регулярных выражений.
"""


print(emails_list[1])