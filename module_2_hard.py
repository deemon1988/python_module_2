import random

numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
random_number = random.choice(numbers)

def find_pairs(n) -> str:
    pairs = []
    for i in range(1, 21):
        if i == n:
            break
        for j in range(i + 1, 21):
            if j == n:
                break
            summ = i + j
            if summ > n:
                break
            elif n % summ == 0:
                pairs.extend((i, j))
    result = ''.join(map(str,pairs))
    return result


print("n:", random_number, "result:", find_pairs(random_number))

