import random

list_numbers =[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
n = random.choice(list_numbers)

result = []
for a in range(0,10):
    res = []
    for b in range(0,10):
        if a!=b and n%(a+b) == 0  :
            res.append(a)
            res.append(b)
    result.append(res)

numbs = [0,1,2,3,4,5,6,7,8,9]

def results(n)->list:

    result_def = []
    a = random.choice(numbs)
    b = random.choice(numbs)
    if a!=b and n % (a+b) == 0:
        result_def.append(a)
        result_def.append(b)
    return result_def

print(results(n))

#  Попарная проверка списка чисел
six = [1,2,1,5,2,4]
pairs = []
pair = []
while six:
    for i in pair:
        six.remove(i)
    if pair:
        pair.clear()
    for j in six:
        pair.append(j)
        pairs.append(j)
        if len(pair) == 2:
            break
print("Все пары проверены")


# Попарная проверка на кратность списка чисел
eight = [1,3,1,7,2,6,3,5]
multiple = []
new_pair=[]
while eight:
    for j in eight:
        if len(new_pair) == 2:
            break
        else:
            new_pair.append(j)
    a = new_pair[0]
    b = new_pair[1]
    if 8 % (a + b) == 0:
        multiple.extend([a,b])
        print(f"Кратная пара: {a}{b}")
        eight.remove(a)
        eight.remove(b)
        new_pair.clear()
    else:
        print(f"Не кратная пара: {a}{b}")
        eight.remove(a)
        eight.remove(b)
        new_pair.clear()