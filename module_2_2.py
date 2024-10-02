first = int(input('Введите 1 число: '))
second = int(input('Введите 2 число: '))
third = int(input('Введите 3 число: '))

if first == second == third:
            print('Вывод: 3')
elif first == second or first == third or second == third:
            print('Вывод: 2')
else:
            print('Вывод: 0')