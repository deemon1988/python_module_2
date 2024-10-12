# Домашняя работа по уроку "Стиль кода часть II. Цикл While"

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
new_list = []
index = 0

while index < len(my_list):
    num = my_list[index]
    if num > 0:
        new_list.append(num)
        index += 1
        print(num)
    elif num < 0:
        break
    else:
        index += 1
        continue