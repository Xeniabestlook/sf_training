a = input("введите число: ")
try:
    b = int(a)
    
except ValueError: 
    print('Вы ввели неправильное число')
else:
    print(f'Вы ввели {b}')
finally:
    print('Выход из программы')