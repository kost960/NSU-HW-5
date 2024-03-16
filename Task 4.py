number = input('Введите число от 1 до 100: ')
if int(number[-1]) == 0 or int(number) == 11:
    print(f'{number} попугаев')
elif int(number[-1]) == 1:
    print(f'{number} попугай')
elif int(number[-1]) < 5:
    print(f'{number} попугая')
else:
    print(f'{number} попугаев')
