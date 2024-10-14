# Домашняя работа по уроку "Функции в Python.Функция с параметром"

def get_matrix(n, m ,value)->list:
    matrix = []
    for i in range(n):
        q = []
        for j in range(m):
            q.append(value)
        matrix.append(q)
    return matrix

result_1 = get_matrix(3,3,10)
result_2 = get_matrix(5,5, 35)
result_3 = get_matrix(3,2, 15)

print(result_1)
print(result_2)
print(result_3)
