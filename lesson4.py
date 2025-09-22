#api
student = {
    'name': 'Alik',
    'age': 18,
    1997: False,
    'education': 'Программист',
    'phone_number': ['123', '4444']
}

student['phone_number'].append('323')
student['phone_number'].reverse()


#Преобразование пар ключ и значений
for key, value in student.items():
    print(f'{key}:{value}')

del student['education']

student['age'] = 19

student['adress'] = 'Tokmok'
print(student)



#print(student['name'])