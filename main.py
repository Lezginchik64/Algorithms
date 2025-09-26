prev = int(input())
cur = int(input())
count = 0

while cur != 0:
    if cur > prev:
        count += 1
    prev = cur
    cur = int(input())
print(count)
