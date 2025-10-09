a = [int(x) for x in input().split()]
k = int(input())
a.pop(k)
print(*a)
