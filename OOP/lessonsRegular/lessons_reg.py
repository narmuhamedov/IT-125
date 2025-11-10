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



print(emails_list[1])