from collections import Counter

n = int(input())
numbers = list(map(int, input().split()))

# Используем Counter для подсчета кол-во встречаемых чисел
counter_numbers = Counter(numbers)
max_prefix_length = 2
for i in range(n - 1, 1, -1):
    # Сортируем Counter по возрастанию и убираем нулевые вхождения
    most_numbers = list(filter(lambda v: v > 0, [x[1] for x in counter_numbers.most_common()]))
    count_number = sum(most_numbers)
    if most_numbers[0] == most_numbers[-1] or (count_number - 1) / most_numbers[0] == len(most_numbers) - 1 or (
            count_number - 1) / most_numbers[-1] == len(most_numbers):
        max_prefix_length = count_number
        break
    counter_numbers[numbers[i]] -= 1
print(max_prefix_length)
