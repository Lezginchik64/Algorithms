a = int(input())
f1 = 0
f2 = 1
for _ in range(a):
    temp = f2  # запомним старый f2
    f2 = f1 + f2  # новый f2 = сумма
    f1 = temp  # новый f1 = старый f2
print(f1)
