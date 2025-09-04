import random
r = random.randint(0,100)
for i in range(1,100):
    a = int(input("Введите число: "))
    if a > r:
        print("Введенное число слишком большое")
        continue
    elif a < r:
        print("Введенное число слишком маленькое")
        continue
    else:
        print("Победа!!!")
        break