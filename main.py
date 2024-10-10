#  Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else."

first = input("Введите первое число:")
second = input("Введите второе число:")
third = input("Введите третье число:")

if first == second and second == third:
    print(f"Первое число ({first}) = Второе число ({second}) = Третье число ({third})")
    print(3)
elif first == second or first == third or second == third:
    print(f"Первое число ({first}), Второе число ({second}), Третье число ({third})")
    print(2)
else: print(0)

