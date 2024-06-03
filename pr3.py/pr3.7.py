a = float(input("Введіть число a: "))
b = float(input("Введіть число b: "))
c = float(input("Введіть число c: "))

negative_count = sum([1 for num in (a, b, c) if num < 0])

print(f"Кількість негативних чисел: {negative_count}")
