# Домашняя работа по уроку "Функции в Python.Функция с параметром"
# Задача "Матрица воплоти":

import random

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def get_matrix(*, n: int, m: int, value: list) -> list:
    matrix = []
    for i in range(n):  #  создаем строку n раз
        rows = []
        for j in range(m):  #  m раз пишем в одну строку
            rows.append(random.choice(value))
        matrix.append(rows) #  заполненную строку добавляем в матрицу
    return matrix

result = get_matrix(n=3, m=3, value=values)
print(result)
print('============================')

def write_matrix(*, matrix: list):
    for k in matrix:
        print(*k)

write_matrix(matrix=result)

