from operator import index

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


prime = []
not_prime = []
list_ = []
for i in numbers:#range(numbers[left], numbers[right]):
    if i == 1:
        print("Excluded value:", i)
        continue
    list_.append(i)
    for j in list_: #range(list_[0], list_[-1]):
        while j in list_:
            if i % j == 0 and i != j:
                if i not in not_prime:      # поставить перед проверкой деления
                    not_prime.append(i)
                    break
                else:
                    break
            elif i == j:    # если равно добавлять в prime
                break
            else: break
            #continue
    if i not in prime and i not in not_prime:
        prime.append(i)


# Простое число имеет только два делителя на 1 и само себя
# Не простое число имеет больше 2х делителей, например 4 - 4:1, 4:4, 4:2
print("Primes:" ,prime)
print("Not Primes:" ,not_prime)