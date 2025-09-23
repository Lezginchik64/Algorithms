# 1 Вариант (не совсем корректный, но рабочий)
count = 0
while True:
    n = int(input())
    if n == 0:
        break
    count += 1
print(count)

# 2 Вариант
count = 0
a = int(input())
while a != 0:
    count += 1
    a = int(input())
print(count)