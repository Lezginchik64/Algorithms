# Вариант 1
y1, x1, y2, x2 = int(input()), int(input()), int(input()), int(input())
if (y1 == y2 + 1 or y1 == y2 - 1) or (x1 == x2 + 1 or x1 == x2 - 1):
    print("YES")
else:
    print("NO")

# Вариант 2
y1, x1, y2, x2 = int(input()), int(input()), int(input()), int(input())
if abs(x1 - x2 ) <= 1 and abs(x1 - x2 ) <= 1:       # abs - это модуль
    print("YES")
else:
    print("NO")