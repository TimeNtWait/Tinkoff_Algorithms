import math

n, m, k = map(int, input().split())
# n - кол-во джунов
# m - кол-во сеньоров
# k - требование к кол-ву проверок
count_checks = n * k  # общее кол-во проверок
minutes = math.ceil(count_checks / m)
print(minutes)
