a = [1,2,1,2,3,3,4]
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)

a = [1, 2, 3]
b = a
print(a is b)

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)