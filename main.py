# Option 1
s = input()
if s.count('f') == 1:
    print(-1)
elif s.count('f') < 1:
    print(-2)
else:
    print(s.find('f', s.find('f') + 1))

# Option 2
s = input()
if s.count("f") == 1:
    print(-1)
elif s.count('f') < 1:
    print(-2)
else:
    print(s.rfind("f"))
