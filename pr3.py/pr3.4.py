x = float(input("Введіть число x: "))
y = float(input("Введіть число y: "))

if x < y:
    x, y = (x + y) / 2, x * y * 2
else:
    y, x = (x + y) / 2, x * y * 2

print(f"Результат: x = {x}, y = {y}")
