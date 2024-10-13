#  Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []
compare_list = []
for i in numbers:
    if i == 1:
        print("Excluded value:", i)
        continue
    compare_list.append(i)
    for j in compare_list:
        if i % j == 0 and i != j:
            not_primes.append(i)
            break
        elif i == j:
            primes.append(i)
            break
        else:
            continue

print("Primes:", primes)
print("Not Primes:", not_primes)

# Простое число имеет только два делителя на 1 и само себя
# Не простое число имеет больше 2х делителей, например 4 - 4:1, 4:4, 4:2