# Генераторы - выражения, позволяющие заполнить список некоторой формулой.

# Пример 1
n = 5
a = [i ** 2 for i in range(n)]

# Пример 2
from random import randrange
n = 10
a = [randrange(1, 10) for i in range(n)]

# Пример 3
a = [input() for i in range(int(input()))]

# Пример 4
a = [i for i in range(5) if i % 2 == 0]
print(*a) # 0 2 4