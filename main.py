a = input().split()
print(*[a[i] for i in range(len(a)) if int(a[i]) % 2 == 0])
