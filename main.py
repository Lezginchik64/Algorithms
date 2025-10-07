m1 = m2 = 0
a = int(input())
while a != 0:
    if a > m1:
        m1, m2 = a, m1
    elif a > m2:
        m2 = a
    a = int(input())
print(m2)