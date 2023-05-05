numbers = list(map(int, input().split()))
# Если последовательность равна отсортированной (по уб. или возр.) то выводим YES иначе NO.
sorted_numbers = sorted(numbers)
if numbers == sorted_numbers or numbers == list(reversed(sorted_numbers)):
    print("YES")
else:
    print("NO")
