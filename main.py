#Option 1
a = [int(x) for x in input().split()]
k, c = [int(x) for x in input().split()]
a = a[:k] + [c] + a[k:]
print(*a)

#Option 2
a = [int(x) for x in input().split()]
k, C = [int(x) for x in input().split()]

a.append(0)                 # Увеличивает список, добавляя 0 в конец
for i in range(len(a) - 1, k, -1):   # Идем в обратном порядке
    a[i] = a[i - 1]                    # Сдвигаем элементы
a[k] = C

print(*a)