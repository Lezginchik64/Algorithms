sum = count = 0
a = int(input())
while a != 0:
    count += 1
    sum += a
    a = int(input())
print(sum / count)