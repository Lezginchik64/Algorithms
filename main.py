# Функции
# Пример 1
def factorial(n):       # n - параметр
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res         # завершает работу функции и возвращает значение переменной res

print(factorial(3))
print(factorial(5))

# Пример 2
def max(a, b):
    if a > b:
        return a
    else:
        return b

print(max(3, 5))
print(max(5, 3))
print(max(int(input()), int(input())))

# Пример 3
def max(a, b):
    if a > b:
        return a
    else:
        return b

def max3(a, b, c):
    return max(max(a, b), c)

print(max3(3, 5, 4))
