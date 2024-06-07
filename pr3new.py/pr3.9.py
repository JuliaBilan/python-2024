def count_integer_numbers():
    a = float(input("Введіть число a: "))
    b = float(input("Введіть число b: "))
    c = float(input("Введіть число c: "))
    
    integer_count = sum([1 for num in (a, b, c) if num.is_integer()])
    
    return integer_count

result = count_integer_numbers()

print(f"Кількість цілих чисел: {result}")
