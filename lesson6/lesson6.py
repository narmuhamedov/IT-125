# Функции - некая формула в математике

# *args , **kwargs
# def meal(**kwargs):
#     return kwargs

# result = meal(breakfast='english breakfast', lunch='Soup', dinner='Stake')

# for k,v in result.items():
#     print(f'{k}-{v}')

# print(result)



# def numbers(*args):
#     return sum(args)


# result = numbers(1,3,45,6,7,8,9,10, 100, 120, 24034, 234340)
# print(result)




# def computer(acer, asus = 12):
#     return f'computer quantity today - {acer} {asus}'

# result = computer(24, 44)
# print(result)



# def greeting(name):
#     return f'Hello - {name}'

# name1 = greeting('Peter')
# name2 = greeting('Jane')
# name3 = greeting('Dean')
# name4 = greeting('Sam')

# print(f'{name1}\n{name2}\n{name3}\n{name4}')



# найти среднее значение температуры всех областей КР
# def avarage(temperature):
#     return sum(temperature) / len(temperature)

# temperature = []
# area = 7

# while area != 0:
#      temp = float(input(f'Введите температуру #{8 - area}: '))
#      temperature.append(temp)
#      area -= 1


# result = avarage(temperature)

# print(f'среднее значение всех температур в КР на сегодня равно - {round(result, 2)}')






# def square(a, b):
#     return a*b

# result = square(a=int(input('Введите длинну')), b=int(input('Введите ширину')))
# print(f'Площадь равна = {result}')



