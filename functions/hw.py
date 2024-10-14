# Домашняя работа по уроку "Функции в Python.Функция с параметром"
# Задача "Матрица воплоти":
#
# Напишите функцию get_matrix с тремя параметрами n, m и value, которая будет создавать матрицу(вложенный список)
# размерами n строк и m столбцов, заполненную значениями value и возвращать эту матрицу в качестве результата работы.
import random

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def get_matrix(*, n: int, m: int, value: list) -> list:
    rows = []
    column = []
    for i in range(n):
        rows.append(random.choice(value))
    for j in range(m):
        column.append(j)

    matrix = [rows, column]

    return matrix

print(get_matrix(n=3, m=3, value=values))

my_matrix = get_matrix(n=3, m=3, value=values)
for k in my_matrix:
    print(*k)


def test_matrix():
    rows = [1,2,3]
    columns = [4,5,6]
    matrix = [
        [1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15]
    ]
    for i in rows:
        for j in columns:
            pass
    for k in matrix:
        print(*k)


