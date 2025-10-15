from math import sqrt
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return sqrt(dx**2 + dy**2)

x1, y1 = float(input()), float(input())
x2, y2 = float(input()), float(input())
print(distance(x1, y1, x2, y2))