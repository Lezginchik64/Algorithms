s = input()
first, second = s.find("h"), s.rfind("h")
part1 = s[:first + 1]
part2 = s[second:]
middle = s[first+1:second].replace("h", "H")
print(part1 + middle + part2)


