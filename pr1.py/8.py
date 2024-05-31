import math
def calculate_combinations(n, m):
    if m > n:
        return 0
    return math.factorial(n) // math.factorial(n - m)
n = 25
m = int(input("Введіть свій порядковий номер у журналі: "))
combinations = calculate_combinations(n, m)
print(f"Кількість можливих комбінацій для {m} комірок: {combinations}")