def count_negative_numbers():
    a = float(input("Введіть число a: "))
    b = float(input("Введіть число b: "))
    c = float(input("Введіть число c: "))
    
    negative_count = sum([1 for num in (a, b, c) if num < 0])
    
    return negative_count

result = count_negative_numbers()

print(f"Кількість негативних чисел: {result}")
