weight = int(input("Введите Ваш вес в фунтах: "))
height = int(input("Введите Ваш рост в дюймах: "))
bmi = (weight/(height**2))*703

if (weight/(height**2))*703 < 16:
    print(f'Выраженный дефицит массы тела')
elif (weight/(height**2))*703 < 18.5:
    print(f'Недостаточная масса тела')
elif (weight / (height ** 2)) * 703 < 25:
    print(f'Норма')
elif (weight/(height**2))*703 < 30:
    print(f'Избыточная масса тела')
elif (weight / (height ** 2)) * 703 < 35:
    print(f'Ожирение первой степени')
elif (weight / (height ** 2)) * 703 < 40:
    print(f'Ожирение второй степени')
else:
    print(f'Ожирение третьей степени')