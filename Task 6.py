quantity = input('Введите количество подданых, которые видели улыбку за каждый из 3 дней, через пробел: ')

quantity_split = quantity.split()

if quantity_split[0] == quantity_split[1] and quantity_split[0] == quantity_split[2]:
    print('3')
elif quantity_split[0] == quantity_split[1] or quantity_split[0] == quantity_split[2] or quantity_split[1] == quantity_split[2]:
    print('2')
else:
    print('Количество не повторялось')
