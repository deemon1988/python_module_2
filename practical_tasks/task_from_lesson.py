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
            pairs.append((a, b), )
print(n, pairs)


def unique_pairs(all_pairs) -> list:
    result_1 = all_pairs
    print(result_1 is all_pairs)
    for k in all_pairs:
        a1 = k[0]
        b1 = k[1]
        for g in all_pairs:
            if k == g:
                continue
            a2 = g[1]
            b2 = g[0]
            if a1 == a2 and b1 == b2:
                result_1.remove(g)
    return result_1


result = unique_pairs(pairs)

print("After remove:", result)

str_pairs = "".join(map(str, (*result,)))
print(str_pairs)
