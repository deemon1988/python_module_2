import random


numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
rand_number = random.choice(numbers)


def find_pairs(n) -> tuple:
    result = []
    count = 0
    for i in range(1, 21):  # если i == n, то summ > n -> n % summ != 0
        count += 1
        for j in range(i + 1, 21):  # если j == n, то summ > n -> n % summ != 0
            count += 1
            summ = i + j
            if n % summ == 0:
                result.append((i, j), )
    tuple_ = (*result,)
    print(count)
    return tuple_

print(find_pairs(rand_number))

