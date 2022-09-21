# """1) Пользователя вводит два числа A и B, нужно вывести сумму чисел в диапазоне от A до B.
# 2) Пользователь вводит два числа A и B, нужно вывести сумму всех четных чисел в диапазоне от A до B.
# 3) Пользователь вводит два числа A и B, нужно вывести прямоугольник со сторонами A и B с помощью символа '*' используя цикл.
# В коде можно использовать символ '*' только один раз.
# 4) Запросить у пользователя число N, вывести треугольник шириной N используя символ '*'.
# Input:
# N = 6
# Output:
# ******
# *****
# ****
# ***
# **
# *
# """

# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# sum = 0
# while a < b:
#     sum += a
#     a += 1
# print(sum)

# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# while a % 2 == 0:
#         sum += a
#     a +=1
# print(sum)
# x = "*"
# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# while a

# N = int(input('enter n '))
# star = "*"
# while N > 0:
#     print(N * star)
#     N -= 1

# N = int(input('enter n '))
# star = "*"
# a = N
# i = 0
# while i < N:
#     i += 1
#     a -= 1
#     print(" " * a, i * star, sep = "")
# print('ok')

# N = int(input('enter n '))
# star = "*"
# a = N
# while N > 0:
#     print(N * star)
#     N -= 1

# # 4
# N = int(input('enter n '))
# star = "*"
# a = N
# i = 0
# while i < N:
#     i += 1
#     a = N - i
#     print(" " * a, i * star, sep="")
# #3
# N = int(input('enter n '))
# star = "*"
# a = 0
# while N > 0:
#     print(" " * a, N * star, sep="")
#     N -= 1
#     a += 1
#
# #2
# N = int(input('enter n '))
# star = "*"
# i = 0
# while i < N:
#     i += 1
#     print(i * star)

#1
N = int(input('enter n '))
star = "*"
while N > 0:
    print(N * star)
    N -= 1

#2
N = int(input('enter n '))
star = "*"
i = 0
while i < N:
    i += 1
    print(i * star)

#3
N = int(input('enter n '))
star = "*"
a = 0
while N > 0:
    print(" " * a, N * star, sep="")
    N -= 1
    a += 1

# 4
N = int(input('enter n '))
star = "*"
a = N
i = 0
while i < N:
    i += 1
    a = N - i
    print(" " * a, i * star, sep="")

