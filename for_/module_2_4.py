
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

prime = []
not_prime = []
compare_list = []
for i in numbers:
    if i == 1:
        print("Excluded value:", i)
        continue
    compare_list.append(i)
    for j in compare_list:
        if i % j == 0 and i != j:
            not_prime.append(i)
            break
        elif i == j:
            prime.append(i)
            break
        else:
            continue

print("Primes:" ,prime)
print("Not Primes:" ,not_prime)

# Простое число имеет только два делителя на 1 и само себя
# Не простое число имеет больше 2х делителей, например 4 - 4:1, 4:4, 4:2
