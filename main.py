# Вариант 1
def power(a, n):
    c = 1
    for _ in range(n):
        c *= a
    return round(c, 3)

a = float(input())
n = int(input())
print(power(a, n))

# Вариант 2
def power(a, n):
    return a**n

a = float(input())
n = int(input())
print(power(a, n))