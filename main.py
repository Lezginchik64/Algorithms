#Вариант 1
a = int(input())
f1 = 0
f2 = 1
for _ in range(a):
    oldf2 = f2
    f2 = f1 + oldf2
    f1 = oldf2
print(f1)

#Вариант 2
for _ in range(a):
    f1, f2 = f2, f1 + f2
print(f1)