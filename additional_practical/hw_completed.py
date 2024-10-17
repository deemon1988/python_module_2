import random

from functions.module_2_5 import result_1

numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
n = random.choice(numbers)


def find_pairs(rand_number) -> tuple:
    result = []
    for i in range(1, 21):  # если i == n, то summ > n -> n % summ != 0
        for j in range(i + 1, 21):  # если j == n, то summ > n -> n % summ != 0
            summ = i + j
            if rand_number % summ == 0:
                result.append((i, j), )
    tuple_ = (*result,)
    return tuple_


string = ''
for a in numbers:
    string += str(a)
print(string)

find_pairs(5)
print("for 5:", find_pairs(5))

area = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
for i in area:
    print(*i)


def print_numbers(args):
    str1 = ''
    for j in args:
        str1 += str(*j)
    print("Print numbers:", str1)


list_ = [[123], [124124], [1515]]

print_numbers(list_)


def find_pairs1(rand_number) -> tuple:
    result = []
    is_divisor = True
    while is_divisor:
        for i in range(1, 21):  # если i == n, то summ > n -> n % summ != 0
            if i == rand_number:
                break
            for j in range(i + 1, 21):  # если j == n, то summ > n -> n % summ != 0
                if j == rand_number:
                    break
                summ = i + j
                if summ > rand_number:
                    is_divisor = False
                    break
                elif rand_number % summ == 0:
                    result.append((i, j),)
            if not is_divisor:
                break
    tuple_ = (*result,)
    return tuple_


print(find_pairs1(5))
