numbers_input = input('Введите высоты башен: ')

numbers = numbers_input.split()

if int(numbers[0]) > int(numbers[1]):
    if int(numbers[1]) > int(numbers[2]):
        print(f'{numbers[0]} {numbers[1]} {numbers[2]}')
    elif int(numbers[0]) > int(numbers[2]):
        print(f'{numbers[0]} {numbers[2]} {numbers[1]}')
    else:
        print(f'{numbers[2]} {numbers[0]} {numbers[1]}')

else:
    if int(numbers[0]) > int(numbers[2]):
        print(f'{numbers[1]} {numbers[0]} {numbers[2]}')
    else:
        if int(numbers[1]) > int(numbers[2]):
            print(f'{numbers[1]} {numbers[2]} {numbers[0]}')
        else:
            print(f'{numbers[2]} {numbers[1]} {numbers[0]}')