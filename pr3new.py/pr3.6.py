def process_numbers(a, b):
    if a != b:
        a = b = max(a, b)
    else:
        a = b = 0
    return a, b

def main():
    a = int(input("Введіть число a: "))
    b = int(input("Введіть число b: "))
    
    a, b = process_numbers(a, b)
    
    print(f"Результат: a = {a}, b = {b}")

if __name__ == "__main__":
    main()
