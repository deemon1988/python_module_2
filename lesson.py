from math import factorial

# Формула сочетаний
def combinations(*, numbers: list, num_of_comb: int) -> int:
    n = len(numbers)
    m = num_of_comb
    return int(factorial(n) / (factorial(m) * factorial(n - m)))


print(combinations(numbers=[1, 2, 3, 4, 5, 7], num_of_comb=2))
