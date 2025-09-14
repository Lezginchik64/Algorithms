from math import pi

a, r = float(input()), float(input())
pi = round(pi, 2)
print(round((a ** 2) - pi * (r ** 2), 6))
