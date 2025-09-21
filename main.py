# Вариант 1
n = int(input())
i = 1                   # i - степень двойки
while 2 ** i <= n:
    i += 1
print(i - 1, 2 ** (i - 1))

# Вариант 2
n = int(input())
deg, two = 0, 1             # deg - степень двойки, two - результат двойки в степени.
while two * 2 <= n:         # two равен 1, потому что 2 в степени 0 = 1
    deg += 1
    two *= 2
print(deg, two)

