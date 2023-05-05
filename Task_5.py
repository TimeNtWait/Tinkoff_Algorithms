n = int(input())
numbers = list(map(int, input().split()))

# По условию задачи не ясно как обрабатывать число 0. По сути это считается как отрезок от i до j, где i=j
# Чтобы не хранить отдельно подотрезки будем просто в массиве для каждого числа записывать индекс конца подотрезка
segments = [n + 1] * n
# Используем два указателя чтобы найти подотрезки с нулевой суммой
for l in range(n - 1):
    sub_sum = numbers[l]
    r = l
    # двигаем правый указатель и ищем те случаи когда сумма подотрезка будет равна 0
    while sub_sum != 0 and r < n - 1:
        r += 1
        sub_sum += numbers[r]
    if sub_sum == 0:
        segments[l] = r
count_segments = 0
# Подсчитываем кол-во отрезков содержащих найденные подотрезки
for l in range(n - 1):
    is_include_segment = False
    r = l
    min_r = n + 1
    # двигаем правый указатель пока не найдем хотя бы одно вхождение нужного подотрезка
    while not is_include_segment and r < n:
        min_r = min(min_r, segments[r])
        if r == min_r:
            is_include_segment = True
            break
        r += 1
    # если есть нужный отрезок внутри диапозона, тогда все остальные диапозона до конца списка включат найденный отрезок
    if is_include_segment:
        count_segments += n - r
print(count_segments)
