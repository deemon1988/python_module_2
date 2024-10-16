import random

n = random.choice([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
result = []
pairs = []
for a in range(1, 21):
    for b in range(1, 21):
        if a == b:
            continue
        summ = a + b
        if n % summ == 0:
            pairs.append((a, b),)
print(n, pairs)


def unique_pairs(all_pairs):
    sum_1 = 0
    for k in all_pairs:
        for q in k:
            sum_1 += q


sums_1 = 0
sums_2 = 0
is_repeated = False

for k in pairs:
    a1 = k[0]
    b1 = k[1]
    for g in pairs:
        if k == g:
            continue
        a2 = g[1]
        b2= g[0]
        if a1 == a2 and b1 == b2:
            is_repeated = True
            pairs.remove(g)

print("After remove:", pairs)

str_pairs = "".join(map(str, (*pairs,)))
print(str_pairs)


