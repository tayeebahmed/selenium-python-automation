# is_hot = False
# is_cold = False
# if is_hot:
#     print("It's a hot day ")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day ")
#     print("wear warm clothes")
# else:
#     print("It's a lovely day ")
 # print("Enjoy your Day")
# price = 1000000
# good_credit = True
# if good_credit:
#     Down_payment = price * 0.10
# else:
#     Down_payment = price * 0.20
# print(f"Down payment: ${Down_payment}")
# high_income = True
# good_credit = False
# if high_income or good_credit:
#     print("eligible for loan")
# else:
#     print("not eligible for loan")
# good_credit = True
# criminal_record = True
#
# if good_credit and  not criminal_record:
#     print("Eligible for loan")
#whileloop
from xml.dom.minidom import ProcessingInstruction


# i = 1
# while i <= 10:
#     print('*' * i)
#     i = i + 1
# print("Done")
# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print('You Won!')
#         break
# else:
#     print('You Lose!')
# command = ""
# started = False
# while True:
#     command = input("Enter Command,  ").lower()
#     if command == "start":
#         if started:
#             print("car already started")
#         else:
#             started = True
#             print("car started...")
#     elif command == "stop":
#         if not started:
#             print("car already stopped")
#         else:
#             started = False
#             print("car stopped...")
#     elif command == "help":
#         print("""
# start - start the car
# stop - stop the car
# exit - quit
#         """)
#     elif command == "exit":
#         break
#     else:
#         print("command not recognized")

# For Loop
# Prices = [10, 20, 30, 60]
# total = 0
# for price in Prices:
#     total = total + price
# print (f"total is {total}")
#nested loop
# for x in range(1,11):
#     for y in range(1,11):
#         print(f'({x}, {y})')
# numbers = [2, 2, 2, 2, 6]
# for number in numbers:
#     output = ""
#     for count in range(number):
#         output += "x"
#     print(output)
#Lists
# names = ['jon', 'don', 'gon', 'bon']
# names[1] = 'yon'
# print (names[1:])
# print (names)

# for number in numbers:
#     if number > Max:
#         Max = number
# print (Max)
# numbers = [3, 7, 8, 9, 5, 8, 0, 28]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print (uniques)
#dictionaries
# customer1 = {
#     'name' : 'Tayeeb Ahmed',
#     'email' : 'tayeebahmed60@gmail,com',
#     'contact' : '9606168047'
# }
#
# customer2 = {
#     'name' : 'John Smith',
#     'email' : 'johnsmith@gmail,com',
#     'Age' : 23,
#     'is verfiried' : True,
#     'contact' : '9602222247'
# }
# customer2['name'] = 'Don bosco'
# print(customer2['name'])
#
# def greet_user(first_name, last_name):
#     print(f'Hello {first_name} {last_name}')
#     print('How are you?')
#
# print('start')
# greet_user(last_name='Tayeeb', first_name='Ahmed')
# print('end')