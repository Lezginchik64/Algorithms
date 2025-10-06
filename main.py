# Вариант 1
s = input()
n = int(input())
english = "abcdefghijklmnopqrstuvwxyz"
count = ""
for i in s:
    index = english.find(i)                     # Ищем индекс введенной буквы
    new_index = (index + n) % len(english)      # прибавляем к индексу n, делим на длину алфавита, чтобы проходить по нему заново
    res = english[new_index]                    # находим новую букву с новым индексом
    count += res                                # добавляем в счетчик
print(count)

# Вариант 2
from string import ascii_lowercase              # импорт строки 'abcdefghijklmnopqrstuvwxyz'
s = input()
n = int(input()) % 26                           # получаем сдвиг и нормализуем его в диапазон 0-25
res = ''
for x in s:
    res += ascii_lowercase[(ascii_lowercase.find(x) + n) % 26]          # ascii_lowercase.find(x) - находим позицию символа в алфавите
print(res)                                                              # + n - сдвигаем позицию на значение n
                                                                        # % 26 - обеспечиваем циклический сдвиг (если вышли за 'z', возвращаемся к 'a')
                                                                        # ascii_lowercase[] - получаем новый символ из алфавита по вычисленной позиции
