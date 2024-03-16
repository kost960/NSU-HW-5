number = input('Введите число: ')
check_number = number[::-1]
if check_number == number:
    print('Настоящее')
else:
    print('Кривое')