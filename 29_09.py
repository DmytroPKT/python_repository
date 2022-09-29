"""Напишите программу где пользователь вводит пароль, а программа проверяет сложность пароля и выводит свой результат в оценочной шкале от 1 до 5.
1 - у пользователя пароль == 'qwerty' or 'admin' или пароль пустой
2 - у пользователя только цифры или спец. символы или все буквы в верхнем или нижнем регистре
3 - у пользователя есть буквы в нижнем регистре и цифры
4 - у пользователя есть цифры, буквы нижнего и верхнего регистра
5 - у пользователя есть цифры, буквы нижнего и верхнего регистра, спец. символы и длинна пароля больше 8 символов"""

password = input('Enter your password: ')
lvl = 0  # Password complexity
simple = 'adminqwertyuserpasswordpaswordpswrdpsw0rdpassw0rdpasw0rd'
is_lower_letter = False
is_upper_letter = False
is_digit = False
is_specific_symbol = False

for chars in password:  # Password chars counting
    if chars.islower():
        is_lower_letter = True
    elif chars.isdigit():
        is_digit = True
    elif chars.isupper():
        is_upper_letter = True
    else:
        is_specific_symbol = True

total = is_specific_symbol + is_digit + is_upper_letter + is_lower_letter


if password.lower() in simple or len(password) < 4:
    lvl = 1
elif total == 4 and len(password) > 8:
    lvl = 5
elif len(password) >= 8 and total >= 3:
    lvl = 4
elif len(password) >= 6 and total >= 2:
    lvl = 3
elif len(password) >= 4 and total >= 1:
    lvl = 2

print(f'Your password complexity level - {lvl}')
