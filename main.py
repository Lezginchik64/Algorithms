a = int(input())
f1, f2 = 0, 1
i = 1
while f2 < a:                 # Цикл работает до числа Фибоначчи
    f1, f2 = f2, f1 + f2
    i += 1
if a == f2:
    print(i)
else:
    print(-1)