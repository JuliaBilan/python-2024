def find_divisors():
    a = int(input("Введіть число a: "))
    b = int(input("Введіть число b: "))
    c = int(input("Введіть число c: "))
    k = int(input("Введіть число k: "))
    
    divisors = [num for num in (a, b, c) if num % k == 0]
    
    return divisors

result = find_divisors()

print(f"Число k є дільником чисел: {', '.join(map(str, result))}")
