N = int(input("Введіть кількість чисел: "))

if N <= 0:
    print("Кількість чисел повинна бути більше нуля!")
else:
    max_number = float('-inf')

    for i in range(N):
        number = float(input(f"Введіть число {i + 1}: "))
        if number > max_number:
            max_number = number

    print("Найбільше число:", max_number)
