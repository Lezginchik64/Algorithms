a = [int(x) for x in input().split()]
idx_min = a.index(min(a))           # Индекс макс или мин используем тогда,когда нужно менять элементы местами
idx_max = a.index(max(a))
a[idx_min], a[idx_max] = a[idx_max], a[idx_min]
print(*a)