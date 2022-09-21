# nn_as = int(input('sddsds: '))
# unit = int(nn_as % 10)
# ten = int((nn_as % 100) / 10)
# hun = int(nn_as / 100)
# final = unit * 100 + ten * 10 + hun
# print(final)

# First one
# a = float(input('Enter number a:'))
# b = float(input('Enter number b:'))
# c = float(input('Enter number c:'))
# if a > 10 and b > 10 and c > 10 and a % 3 == 0 and b % 3 == 0:
#     print('yes')
# else:
#     print('no')
#
# # Second one
# a = int(input('Enter number a:'))
# b = int(input('Enter number b:'))
# c = int(input('Enter number c:'))
# if a > b and a > c:
#     print('max - a')
# elif b > a and b > c:
#     print('max - b')
# elif c > a and c > b:
#     print('max - c')
# else:
#     print('no way')

# Third one
# while True:
#     try:
#         input_number = int(input('Enter number: '))
#         first_digit = input_number//100
#         second_digit = (input_number % 100)//10
#         third_digit = input_number % 10
#         reversed_number = third_digit*100 + second_digit*10 + first_digit
#         if 99 < input_number < 1000:
#             print(reversed_number)
#         elif input_number == 1488:
#             exit('bye bye lame ass')
#         else:
#             print('Sorry, this code only for 3 digit numbers')
#     except ValueError:
#         print('for the fuck sakes, enter NUMBER ONLY, stupid piece of scrap')







# l = list()
#
# EXIT_COMMAND = 'calc'
#
# print(f'Type `{EXIT_COMMAND}` when you ready for calculating')
#
# while True:
#     num = input(f'Enter number or "{EXIT_COMMAND}": ')
#     if num != int() and float():
#         break
#     if num == EXIT_COMMAND:
#         exit('max value: ' + str(max(l)))
#
#     l.append(int(num))









# number = int(input('Enter number: '))
# print(12 >= number >= 1 or 300 >= number >= 13 and number != 13)
# print(True or False and True)

# print('ll' not in 'Hello')
# secret_number = 42
# number = int(input('Enter number: '))
# if number == secret_number:
#     print('Victory')
# elif 5 >= number >= 2:
#     print('ahahaha')
# elif 10 >= number >= 6:
#     print('no way')
# elif 14 >= number >= 11:
#     print('no no no')
# else:
#     print("loool")
# secret_number = 3
# number = int(input('Enter number: '))
# if number == secret_number:
#     exit()
# number_2 = int(input())
#
# if number_2 == 5:
#     exit()
# number_3 = int(input())
#
# if number_3 == 3444:
#     print('very nice')
# result = ''
# num = int(input())
# if num == 1:
#     result = 'zima'
#     print(result)
# elif num == 2:
#     result = 'vesna'
#     print(result)
# elif num == 3:
#     result = 'leto'
#     print(result)
# elif num == 4:
#     result = 'osen'
#     print(result)
# else:
#     exit()
#
# print(f'Result: {result}')

# print(int((input()[::-1]))
# 321
# nn_as = int(input('sddsds: '))
# unit = int(nn_as % 10)
# ten = int((nn_as%100)/10)
# hun = int(nn_as/100)
# final = unit*100+ten*10+hun
# print(final)

# a = input()

# if len(a) != 4:
#     exit('Gedfdf dfdf ')
#     raise Exception('only 3 symbols, looser')
#
# print(a[::-1])

# calculator karabul
# try:
#     menu = '''Menu of calculator:
# 1 - Add
# 2 - Subtract
# 3 - Multiply
# 4 - Divide
# 5 - Exponentiation
# Select operation: '''
#
#
#     number1 = float(input('Enter first number: '))
#     user_choice = int(input(menu))
#     number2 = float(input('Enter second number: '))
#     if user_choice in range(1, 6):
#         if user_choice == 1:
#             result = number1 + number2
#         elif user_choice == 2:
#             result = number1 - number2
#         elif user_choice == 3:
#             result = number1 * number2
#         elif user_choice == 4:
#             result = number1 / number2
#         elif user_choice == 5:
#             result = number1 ** number2
#     else:
#         print("Invalid Input")
#
#     print(f'Result: {result}')
#
# # Error info
# except ValueError:
#     print("Do not enter letters or symbols(except dot). Please, restart the program and enter NUMBER")

# kvadraty
# try:
#     number = int(input("Enter number: "))
#
# # num_in_square started print from 1
#     num_in_square = 1
#     for i in range(1, number + 1):
#         num_in_square = i ** 2
#         i += 1
#         if number >= num_in_square:
#             print(num_in_square, end=" ")
#
# # Error info
# except ValueError:
#     print("Do not enter letters or symbols. Please, restart the program and enter NUMBER")
# simple not simple
# try:
#     number = int(input("Enter number: "))
#
# # prime numbers are greater than 1
#     if number > 1:
#         for i in range(2, number):
#             if (number % i) == 0:
#                 print("It's not a prime number")
#
# # operator break used for stop cycle if stateman (num%i==0) satisfied
#                 break
#         else:
#             print("It's a prime number")
#
# # if input number is less than or equal to 1, it is not prime
#     else:
#         print("It's not a prime number")
#
# # Error info
# except ValueError:
#     print("Do not enter letters or symbols. Please, restart the program and enter NUMBER")

n = int(input())
for i in range(n-1):
    numwhite = n-i
    print(' ' * numwhite + '*' * i + '*' * i)




