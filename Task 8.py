knats = int(input('Введите количество кнатов: '))

knats_after_point = knats % 29
sikls = knats % 493//29
galleon = knats//493


if galleon == 0:
    print(f'{sikls} сиклей\n'
          f'{knats_after_point} кнатов')
elif sikls == 0:
    print(f'{galleon} галлеонов\n'
          f'{knats_after_point} кнатов')
elif knats_after_point == 0:
    print(f'{galleon} галлеонов\n'
          f'{sikls} сиклей')
else:
    print(f'{galleon} галлеонов\n'
          f'{sikls} сиклей\n'
          f'{knats_after_point} кнатов')