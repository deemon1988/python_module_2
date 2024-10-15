#  Проверка на чётность всех возможных пар чисел
#  из диапазона  от 0 до 9 a != b
import random

list_numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
n = 20#random.choice(list_numbers)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
multiple = []
pair =[]

#  Записывать каждую пару кратных чисел в виде списка, доабвлять в основной список
#  Проверять пару чисел

# a = 0
# b = 0

for i in numbers:
    a = i
    # if b == 1:
    #     if a + b > n:
    #         break
    for j in numbers:
        repeated_pair = False
        b = j
        if a+b > n:
            break
        if a==b:
            continue
        for k in pair:
            if a == k[1] and b == k[0]:
                print(f"Повторная пара: {a}{b}")
                repeated_pair = True
                break
        if n % (a + b) == 0 and repeated_pair == False:        #  Повторное значение 43 Проверять на уникальность
            multiple.extend([a, b])
            pair.append((a, b))
            print(f"Кратная пара: {a}{b}")

print(f"Кратные пары для числа {n}: {multiple}")
print(*multiple)
string = "".join(map(str,multiple))
pairs = "13141911923282183731746416515614713812911"
print(string==pairs)
print("Пары чисел",string)

tuple_ = (*multiple,)
print(tuple_)


