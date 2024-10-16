
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = False

for i in numbers:
    if i == 1:
        continue
    for j in range(2,15):       #  число 2 сразу = 2 куда его учитывать ?
        if i % j != 0 and j < i:
            continue               #  можно прерывать цикл
        elif i == j:
            is_prime = True  # зачем использовать ? можно использовать булево занчение
            primes.append(i)
            break
        else:                      # найден делитель, число не простое
            is_prime = False
            not_primes.append(i)
            break

print("Primes:",primes)
print("Not Primes:",not_primes)

