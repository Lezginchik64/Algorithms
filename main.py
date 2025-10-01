# Вариант 1
s = input()
ind = (len(s) + 1) // 2
part1 = s[:ind]
part2 = s[ind:]
print(part2 + part1)

# Вариант 2
s = input()
mid = len(s) // 2
if len(s) % 2 != 0:
    print(s[mid+1:] + s[:mid+1])
else:
    print(s[mid:] + s[:mid])
