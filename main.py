n, m, k = int(input()), int(input()), int(input())
s = n * m
if (k % n == 0 or k % m == 0) and k < s:
    print("YES")
else:
    print("NO")
