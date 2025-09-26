# Вариант 1
a = int(input())
m = countm = 0
while a != 0:
    if a > m:
        m, countm = a, 1   # нашли новый максимум → обновили m и сбросили счётчик
    elif a == m:
        countm += 1        # нашли ещё одно вхождение максимума
    a = int(input())
print(countm)

# Вариант 2
m = 0
c = 1
a = int(input())
while a != 0:
    if a > m:
        m = a
    a = int(input())
    if a == m:
        c += 1
print(c)


