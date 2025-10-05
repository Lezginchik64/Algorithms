s = input()
res = ""
for i in range(len(s)):
    if i % 3 != 0:
        res += s[i]       # Складываем в res буквы, у которых индекс не делится на 3
print(res)



