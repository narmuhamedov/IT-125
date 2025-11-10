# Основные принципы ООП 
# Полиморфизм Наследование и Абстракция Инкапсуляция 

# #Полиморфизм
# class Bird:
#     def make_sound(self):
#         print('Чирик Чирик')

# class Cow:
#     def make_sound(self):
#         print('МУУУУУУУ')

# animals = [Bird(), Cow()]

# for animal in animals:
#     animal.make_sound()





#Абстракция
# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area():
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
    
#     def area(self):
#         return 3.14 * self.radius ** 2
    
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
    
#     def area(self):
#         return self.width * self.height

# shapes = [Circle(5), Rectangle(4,6)]

# for s in shapes:
#     print(s.area())
        










#Инкапсуляция

# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance #Приватность данных

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
        
#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
    
#     def get_balance(self):
#         return self.__balance


# acc = BankAccount('Иван', 1000)
# print(acc.name)
# print(acc.deposit(500))
# print(acc.get_balance)

    