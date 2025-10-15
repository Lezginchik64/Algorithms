def greet(name):
    print(f'Hello, {name}!')
N = int(input())
names = [input() for _ in range(N)]
for name in names:
    greet(name)