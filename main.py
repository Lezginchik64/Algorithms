# Вариант 1
def world_sorting(s):
    s.sort()
    return s
s = input().split()
print(*world_sorting(s))

# Вариант 2
def word_sorting(s):
    return ' '.join(sorted(s.split()))

print(word_sorting(input()))