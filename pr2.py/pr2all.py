a = 10
b = 5

print(a > 0 and b > 0)  
print(a == 10 and b == 5)  
print(a < 0 and b > 0) 
print(a > 10 and b > 0) 

print(a > 0 or b < 0) 
print(a == 10 or b == 10)  
print(a < 0 or b < 0)  
print(a > 10 or b > 10)  

str1 = "hello"
str2 = "world"
print(str1 == "hello" and str2 == "world")  
print(len(str1) == 5 and len(str2) == 5)  
print(str1 == "hello" and str2 == "python") 
print(len(str1) == 4 and len(str2) == 5) 

c = 7
if c > 0:
    print("Значення змінної більше 0")
c = -3
if c > 0:
    print("Значення змінної більше 0")
    
c = 7
if c > 0:
    print(1)
else:
    print(-1)
c = -3
if c > 0:
    print(1)
else:
    print(-1)

a = 9
b = 4
if a > b:
    c = a - b
elif a < b:
    c = a + b
else:
    c = a
print(c)

# перші числа ряду Фібоначчі
a, b = 0, 1
while b < 100: 
    print(b, end=' ')
    a, b = b, a + b
print()

# від 5-го до 20-го
fib_sequence = []
a, b = 0, 1
count = 0

while count < 20:
    fib_sequence.append(b)
    a, b = b, a + b
    count += 1

# Виведення
for number in fib_sequence[4:20]:
    print(number, end=" ")
print()

# Виведення парних чисел від 0 до 20
for i in range(0, 21, 2):
    print(i, end=" ")
print()

# кожного третього числа від -1 до -21
for i in range(-1, -22, -3):
    print(i, end=" ")
print()
