def print_even_numbers(n, m):
    for i in range(-n, n + 1, m):
        if i % 2 == 0:
            print(i)
n = int(input("Введіть значення n: "))
m = 5
print_even_numbers(n, m)