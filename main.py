#Option 1
a = [int(x) for x in input().split()]
petya = int(input())
for i in range(len(a)):
    if petya > a[i]:
        print(i + 1)
        break
else:
    print(len(a) + 1)

#Option 2
a = [int(x) for x in input().split()]
X = int(input())
pos = 0
while pos < len(a) and X <= a[pos]:
    pos += 1
print(pos + 1)