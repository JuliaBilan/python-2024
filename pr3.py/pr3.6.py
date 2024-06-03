a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))

if a != b:
    a = b = max(a, b)
else:
    a = b = 0

print(f"Результат: a = {a}, b = {b}")
