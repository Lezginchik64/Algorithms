a = [int(x) for x in input().split()]
count = 1
for i in range(1, len(a)):
    if a[i] != a[i - 1]:
        count += 1
print(count)