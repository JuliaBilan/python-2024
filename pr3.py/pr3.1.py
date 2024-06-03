x = float(input("Введіть перше число: "))
y = float(input("Введіть друге число: "))
z = float(input("Введіть третє число: "))

def process_number(num):
    if num >= 0:
        return num ** 2
    else:
        return num ** 4

x_result = process_number(x)
y_result = process_number(y)
z_result = process_number(z)

print(f"Оброблені числа: {x_result}, {y_result}, {z_result}")
