# Option 1
def election(x, y, z):
    if x + y + z >= 2:
        return 1
    else:
        return 0

x, y, z = [int(x) for x in input().split()]
print(election(x, y, z))

# Option 2
def election(x, y, z):
    votes = [x, y, z]
    if votes.count(1) > votes.count(0):
        return 1
    else:
        return 0
x, y, z = [int(x) for x in input().split()]
print(election(x, y, z))