quantity = input('Введите данные станций (N, K, M соответственно): ')

quantity_split = quantity.split()

if int(quantity_split[1]) < int(quantity_split[2]):
    print(abs(int(quantity_split[2]) - int(quantity_split[1])))
else:
    print(int(quantity_split[2]) - abs(int(quantity_split[1]) + (int(quantity_split[0])) - 1))
