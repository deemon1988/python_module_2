#  Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []
is_prime = False

for i in numbers:
    if i == 1:
        print("Excluded value:", i)
        continue
    for j in range(2,15):
        if i == j:
            is_prime = True
            primes.append(i)
            break
        elif i % j == 0:
            is_prime = False
            not_primes.append(i)
            break

print("Primes:",primes)
print("Not Primes:" ,not_primes)