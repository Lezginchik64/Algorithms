#Option 1
print(*input().split()[::2])

#Option 2
a = input().split()
print(*[a[i] for i in range(len(a)) if i % 2 == 0])
