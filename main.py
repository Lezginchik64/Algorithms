a = [int(x) for x in input().split()]
count = 0
for i in range(1, len(a) - 1):               # Идем от второго до предпоследнего, чтобы сработал a[i + 1]
    if a[i - 1] < a[i] and a[i + 1] < a[i]:
        count += 1
print(count)
