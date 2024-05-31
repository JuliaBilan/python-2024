n = int(input("Введіть ціле число: "))
n1 = n
n2 = int(f"{n}{n}")
n3 = int(f"{n}{n}{n}")
result = n1 + n2 + n3
print(f"Результат обчислення {n} + {n}{n} + {n}{n}{n} дорівнює {result}")
