pin = input('Введите пинкод: ')
if int(pin) < 1000:
        print('ERROR')
elif pin[0] == pin[1] or pin[0] == pin[2] or pin[0] == pin[3] or pin[1] == pin[2] or pin[1] == pin[3] or pin[2] == pin[3]:
    print('ERROR')
elif int(pin) > 9999:
    print('ERROR')
elif int(pin) > 1900 and int(pin) < 2050:
    print('ERROR')
else:
    print('OK')
