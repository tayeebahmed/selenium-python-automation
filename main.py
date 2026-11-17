# import converters
# from converters import kgs_to_lbs
#
# print(kgs_to_lbs(80))
# import Utills
# from Utills import find_max
#
# numbers = [0, 8, 9, 10, 17, 16]
# maximum = find_max(numbers)
# print(maximum)
#
# import ecommerce
# from ecommerce import Shipping
# from ecommerce.Shipping import calc_shipping
#
# calc_shipping()
# from importlib.metadata import files
# from pathlib import Path
#
# path = Path()
# for file in path.glob('*'):
#     print(file)
# class Point:
#     def move(self):
#         print("Moving Point")
#
#     def draw(self):
#         print("Draw")
#
#
# point1 = Point()
# point1.move()
# class mammal:
#     def walk(self):
#         print("Walking")
#
# class dog(mammal):
#     def Bark(self):
#         print("Barking")
#
# class cat(mammal):
#     def meow(self):
#         print("Meowing")
#
#
# dog1 = dog()
# dog1.walk()
# dog1.Bark()
# cat1 = cat()
# cat1.meow()

# import openpyxl as xl
# wb = xl.load_workbook('transactions.xlsx')
# sheet = wb['Sheet_1']
#
# for row in range(2, sheet.max_row + 1):
#     cell = sheet.cell(row, 3)
#     print(cell.value)
# file = open("student.txt", "r")
#
# for line in file:
#     print(line)
#
# file.close()

# file.write("Hello World\n")
# file.write("Tayeeb\n")
# file.write("learn python\n")
# file.close()
#
# file = open("student.txt", "r")
#
# content = file.read()
# print(content)
# file.close()
# with open("student.txt", "r") as file:
#     content = file.read()
#     print(content)
# def save_employees():
#     with open("student.txt", "w") as file:
#         file.write("Hello Tayeeb\n")
#         file.write("learnautomation\n")
#         file.write("All the best\n")
#
# def read_employees():
#     with open("student.txt", "r") as file:
#         print(file.read())
#
#
# save_employees()
# read_employees()

# print(write)
# print(read)
# class Update:
#     def course_update(self):
#         with open("course_progress.txt", "w") as file:
#             file.write("python Essentials - completed\n")
#             file.write("OOP Basics - inprogress\n")
#             file.write("selenium - Pending\n")
#
#
#
#     def course_progress(self):
#         with open("course_progress.txt", "r") as file:
#             print(file.read())
#
# update = Update()
# update.course_update()
# update.course_progress()

try:
    Age = int(input("Age, "))
    income = 20000
    risk = income / Age
    # print(risk)
    print(Age)
# except ZeroDivisionError:
#     print("Age cannot be zero")
except ValueError:
    print("Invalid Age")
finally:
    print("End of the program")