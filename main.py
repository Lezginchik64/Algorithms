#Option 1  -  выполнена неверно, так как элементы списка являются строками
a = input().split()
for i in range(1, len(a)):    # Начинаем от 1, чтобы не было такого a[0] > a[-1]
    if a[i] > a[i - 1]:
        print(a[i], end=' ')

#Option 2
a1 = [int(x) for x in input().split()]  #Преобразуем элементы списка в числа
for i in range(1, len(a1)):
    if a1[i] > a1[i - 1]:
        print(a1[i], end = ' ')