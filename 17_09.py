# number = int(input('ertertertert: '))

# if number % 2 == 1:
#     print('odd')
# else:
#     print('Even')

# is_even = 'Evene' if number %2 == 0 else 'Odd'
#
# print(is_even)

# number = 3
# condition = True
#
# if number % 2 == 0:
#     print(10)
# else:
#     if condition:
#         print(20)
#     else:
#         print(30)
#
# print(10) if number % 2 == 0 else print(20) if condition else print(30)

# number = 0
#
# while number > - 1:
#     print(f'Kol vo iteratsiy : {number +1}')
#     print(number)
#     number += 1

# number = int(input())
#
# while number % 2 != 0:
#     print('error')
#     number = int(input('Entrer number'))
#
# print('correctr')

# number = int(input())
#
# while not 0 <= number <= 10:
#
#     print('error')
#     number = int(input('Entrer number'))
#
# print('correctr')

# while True:
#     number = int(input())
#     if 0 <= number <= 10:
#         break
#     print('error')
# print('number ok')

# # First one
# a = int(input('Enter number a:'))
# b = int(input('Enter number b:'))
# c = int(input('Enter number c:'))
# if a > 10 < b and c > 10 and b % 3 == 0 == a % 3:
#     print('yes')
# else:
#     print('no')

# number = 0
#
# while number <= 49:
#     number += 3
#
#     if number == 50:
#         break
#
#     print(number)
# else:
#     print('done')
#
# print('end')

# First one
# a = int(input('Enter number a:'))
# b = int(input('Enter number b:'))
# c = int(input('Enter number c:'))
# if a > 10 < b and c > 10 and b % 3 == 0 == a % 3:
#     print('yes')
# else:
#     print('no')

# a = int(input('Enter number a:'))
# b = int(input('Enter number b:'))
# star = "*"
# i = 0
# while i < b:

# a = int(input('Enter number for a: '))
# b = int(input('Enter number for b: '))
# sum = 0
# while a <= b:
#     sum = sum + a
#     a += 1
# print('Summa chisel ot a do b: ', sum)
# num = int(input("Пожалуйста, введите число:"))
#
# if num > 1:  # Простое число больше 1
#     for i in range(2, num):
#         os = num % i
#         if os >= 0:
#             print("простое число")
#         else:
#             print(num, "NEПростое число")
# else:
#     print(num, "Не простое число")
# num = int(input("Пожалуйста, введите число:"))
# for i in range(2, num):
#     os = num % i
#
# for i in range(2, num):
#     os = num % i
#     if os >= 1:
#
# else:
#         print(num, "NEПростое число")
# print(num, "Не простое число")
# x = False
# num = int(input("Пожалуйста, введите число:"))
# for i in range(2, num):
#     os = num % i
#     if os == 0:
#         x = False
#         break
# if x:
#     print('not ok')
# else:
#     print(f'{num} is ok')

# num = int(input("Enter number: "))
#
# # To take input from the user
# #num = int(input("Enter a number: "))
#
# # define a flag variable
# flag = False
#
# # prime numbers are greater than 1
# if num > 1:
#     # check for factors
#     for i in range(2, num):
#         if (num % i) == 0:
#             # if factor is found, set flag to True
#             flag = True
#             # break out of loop
#             break
#
# # check if flag is True
# if flag:
#     print(num, "is not a prime number")
# else:
#     print(num, "is a prime number")

# Program to check if a number is prime or not
#
# num = int(input('Enter number '))

# To take input from the user
# num = int(input("Enter a number: "))

# prime numbers are greater than 1
# if num > 1:
#     # check for factors
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
#
# # if input number is less than
# # or equal to 1, it is not prime
# else:
#     print(num, "is not a prime number")

# try:
#     n = int(input("Enter number: "))
#     x = 1
#     for i in range(1, n + 1):
#         x = i ** 2
#         i += 1
#         if n >= x:
#             print(x, end=" ")
# # Error info
# except ValueError:
#     print("Do not enter letters or symbols. Please, restart the program and enter NUMBER")
# 28


# n = int(input("Enter number: "))
# if 11 <= n % 100 <= 14 or 5 <= n % 10 <= 9 or n % 10 == 0:
#     print(f'sobrala {n} gribov')
#     exit()
# if 1 < n % 10 < 5:
#     print(f'sobrala {n} griba')
#     exit()
# if n % 100 != 11 and n % 10 == 1:
#     print(f'sobrala {n} grib')
#     exit()

# try:
#     mushroom = int(input("Введите количество грибов: "))
#     if mushroom > 0:
#         if 5 <= mushroom % 10 <= 9 or mushroom % 10 == 0 or 11 <= mushroom % 100 <= 14:
#             m = "ов."
#         elif 1 < mushroom % 10 < 5:
#             m = "а."
#         elif mushroom == 1 or mushroom % 10 == 1 and mushroom != 11:
#             m = "."
#     else:
#         print("Маша нашла в лесу 0 грибов")
#     print(f"Маша нашла в лесу {mushroom} гриб{m}")
# # Error info
# except ValueError:
#     print("Do not enter letters or symbols. Please, restart the program and enter NUMBER")

# n = int(input('Enter number: '))
# i = 0
# sum = 0
# while i <= n:
#     sum = sum + i
#     i += 1
#
#
# print('summa chisel ot 1 do n: ', sum)

n = int(input('Enter number: '))
while n < 10:
    if n % 2 == 0:
        print('number ' + str(n) + ' is even')
    else:
        print('number ' + str(n) + ' is odd')
    n = n + 1
