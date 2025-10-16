# Вариант 1
def arithmetic_progression(a, d, n):
    an = a + (n - 1) * d
    sn = n * (a + an) // 2
    return sn

a, d, n = [int(x) for x in input().split()]
print(arithmetic_progression(a, d, n))

# Вариант 2
def arithmetic_progression2(a, d, n):
    return (2 * a + (n - 1) * d) * n // 2

a, d, n = [int(x) for x in input().split()]
print(arithmetic_progression2(a, d, n))

# Вариант 3
def arithmetic_progression3(a, d, n):
    total = 0
    for i in range(n):
        total += a + i * d
    return total
a, d, n = [int(x) for x in input().split()]
print(arithmetic_progression3(a, d, n))
