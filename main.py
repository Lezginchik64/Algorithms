s = input()
if s.find("h") > 1:
    print(s[:s.find("h")] + s[s.rfind("h") + 1:])


