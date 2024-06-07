def count_positive_numbers():
    a = float(input("Введіть число a: "))
    b = float(input("Введіть число b: "))
    c = float(input("Введіть число c: "))
    
    positive_count = sum([1 for num in (a, b, c) if num > 0])
    
    return positive_count

result = count_positive_numbers()

print(f"Кількість додатних чисел: {result}")
