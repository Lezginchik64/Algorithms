x = int(input())
y = int(input())
c = 1
while x < y:
    d = x * 0.1
    x += d
    c += 1
    print(x)
print(c)
