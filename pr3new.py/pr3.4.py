def process_numbers(x, y):
    if x < y:
        x, y = (x + y) / 2, x * y * 2
    else:
        y, x = (x + y) / 2, x * y * 2
    return x, y

def main():
    x = float(input("Введіть число x: "))
    y = float(input("Введіть число y: "))
    
    x, y = process_numbers(x, y)
    
    print(f"Результат: x = {x}, y = {y}")

if __name__ == "__main__":
    main()
