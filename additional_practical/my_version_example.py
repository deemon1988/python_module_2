import random

list_numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
n = random.choice(list_numbers)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
pairs_numbers =[]

for i in range(1,21):
    for j in range(i+1,21):
        pair_sum = i + j
        if n % pair_sum == 0:
            pairs_numbers.extend((i, j))

print(*pairs_numbers)
string = "".join(map(str,pairs_numbers))
print(f"Кратные пары для числа {n}: {string}")

pairs = "13141911923282183731746416515614713812911"
print(string==pairs)


tuple_ = (*pairs_numbers,)




