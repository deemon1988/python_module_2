from operator import index

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

left = 1
right = len(numbers) - 1
prime = []
not_prime = []
list_ = []
for i in range(numbers[left], numbers[right]):
    list_.append(i)
    for j in range(list_[0], list_[-1]):
        if i % j == 0:
            not_prime.append(i)
            break
        else:
            prime.append(i)
            break


print(prime)
print(not_prime)