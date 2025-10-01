# Option 1
s = input()
ind = s.find(' ')
word1 = s[:ind]
word2 = s[ind + 1:]
print(word2, word1)

# Option 2
s = input()
if s.count(" ") >= 1:
    print(s[s.find(" ") + 1:] + " " + s[0:s.find(" ")])
