#  поле для игры 3х3

area = [['*', '*', '*'],['*', '*', '*'],['*', '*', '*']]
for i in area:
    print(*i)

is_busy = False

while not is_busy:
    #  игроки ходят поочереди (реализовать через input)
    cross = []
    while len(cross) < 2 and not is_busy:
        #  Сделать отдельно цикл While для row и для cell
        try:
            row = int(input("Ходят крестики. Введите номер строки:"))
        except ValueError:
            continue
        # Здесь проверять через if else
        while row > 3 or row <= 0:
            try:         # исключение ValueError
                row = int(input("Введите номер строки от 1 до 3:"))
            except ValueError:
                continue
        cross.append(row-1)
        #  Сделать отдельно цикл While для row и для cell
        try:
            cell = int(input("Ходят крестики. Введите номер ячейки:"))
        except ValueError:
            continue
        # Здесь проверять через if else
        while cell > 3 or cell <= 0:
            cell = int(input("Введите номер ячейки от 1 до 3:"))
        cross.append(cell-1)
        if area[cross[0]][cross[1]] == 'O' or area[cross[0]][cross[1]] == 'X':
            cross.clear()
            print("Сюда ходить нельзя")
        else:
            area[cross[0]][cross[1]] = 'X'
    #  ничья, если свободные ячейки закончились
    for i in area:
        print(*i)
        if '*' in i:
            continue
        elif i == area[-1] and '*' not in i:
            print("Ходы закончились. Ничья")
            is_busy = True
            break

    zero = []
    while len(zero) < 2 and not is_busy:
        row = int(input("Ходят нолики. Введите номер строки:"))
        while row > 3 or row <= 0:
            row = int(input("Введите номер строки от 1 до 3:"))
        zero.append(row-1)
        cell = int(input("Ходят нолики. Введите номер ячейки:"))
        while cell > 3 or cell <= 0:
            cell = int(input("Введите номер ячейки от 1 до 3:"))
        zero.append(cell - 1)
        #  проверять что ячейка пустая, иначе сюда походить нельзя
        if area[zero[0]][zero[1]] == 'X' or area[zero[0]][zero[1]] == 'O':
            zero.clear()
            print("Сюда ходить нельзя")
        else:
            area[zero[0]][zero[1]] = 'O'

    for i in area:
        print(*i)
        if '*' not in i:
            continue
        elif i == area[-1] and '*' not in i:
            print("Ходы закончились. Ничья")
            is_busy = True
            break



#  победа, если подряд 3 по вертикали или горизонтали или подиагонали

