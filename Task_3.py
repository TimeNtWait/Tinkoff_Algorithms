import math
from collections import Counter

len_string = int(input())
input_string = input().strip()

min_length = math.inf
counter_string = Counter({"a": 0, "b": 0, "c": 0, "d": 0})
# Используем два указателя чтобы найти подстроку удовлетворящую тербованиям
j = 0
for i in range(len_string - 1):
    # двигаем правый указатель пока не найдем символ который обеспечивает выполнение условия
    while counter_string.most_common()[-1][1] == 0 and j < len_string:
        counter_string[input_string[j]] += 1
        j += 1
    if counter_string.most_common()[-1][1] > 0:
        min_length = min(min_length, j - i)
    # убираем i-ый элемент т.к. на следующей иттерации i сдвигаем вправо на 1
    counter_string[input_string[i]] -= 1

if math.isinf(min_length):
    print(-1)
else:
    print(min_length)
