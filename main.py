#Option 1
a = input().split()
for i in range(1, len(a)):    # Начинаем от 1, чтобы не было такого a[0] > a[-1]
    if a[i] > a[i - 1]:
        print(a[i], end=' ')

#Option 2
a = [int(x) for x in input().split()]
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i], end = ' ')