# Определяем функцию для нахождения всех уникальных пар чисел и проверки делимости
import random

list_numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
n = 20#random.choice(list_numbers)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def find_pairs(n):
    pairs = []
    for a in range(1, 21):
        for b in range(a + 1, 21):  # Пары (a, b) где a < b для уникальности
            pair_sum = a + b
            if n % pair_sum == 0:
                pairs.append((a, b))
    return pairs

# Пример случайного числа от 3 до 20
random_divisor = 12  # Можно заменить на любое число от 3 до 20

# Нахождение всех пар для числа 12
# unique_pairs = find_pairs(random_divisor)
# print(unique_pairs)
found_pass = find_pairs(n)
print("n = ",n, '\n',found_pass)

