y1, x1, y2, x2 = int(input()), int(input()), int(input()), int(input())
dx, dy = abs(x1 - x2), abs(y1 - y2)
if dx == 2 and dy == 1 or dx == 1 and dy == 2:
    print("YES")
else:
    print("NO")