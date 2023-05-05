import heapq

n, s = map(int, input().split())
scores = []
for _ in range(n):
    l, r = map(int, input().split())
    scores.append((l, r))
idx_median = n // 2

# Чтобы повысить медийный балл достаточно повышать только вторую половину сортированных учеников
# Как вариант алгоритма испоьлзовать кучу для второй половины всех элементов.
# Требуется также учитывать предельное возможное значение баллов у учеников.
# 1. берем из кучи минимум (для второй половины элементов это и будет медиана),
# 2. увеличиваем полученный элемент на 1 если максимальный предельный балл ученеика позволяет
# 3. кладем новое значение обратно в кучу
# Повторяем пока общая сумма не достигнет предела s, либо достигли максимумального предела баллов у медианного ученику
# Если достигли максимума баллов у медианного ученику, то начианем все заново но меняем ученика, для этого сделаем
# верхеуровнеый обход учеников от медианного до 1 по списку

scores = sorted(scores)
# Изначальная сумма
source_sum = sum([x[0] for x in scores])
median_item_score = scores[idx_median]
max_median_score = median_item_score[0]
# Выбираем изначальный набор учеников (вторая половина по возрастанию)
src_selected_scores = scores[idx_median + 1:]
# проходим по оставшейся половине учеников, начиная с медианны и далее по убыванию
for score in list(reversed(scores[:idx_median + 1])):
    # Если максимально-пределльный балл больше текущей макс медианы, то добавляем этого ученика в рассмотрение
    if score[1] > max_median_score:
        selected_scores = []
        src_selected_scores.append(score)
        for item in src_selected_scores:
            heapq.heappush(selected_scores, (item[0], item))
        current_sum = source_sum
        while current_sum < s:
            min_item = heapq.heappop(selected_scores)
            # Достигнут макс.предел баллов для ученика, исключаем его из выбранных оценок и переходим к следующему
            if min_item[0] == min_item[1][1]:
                src_selected_scores.remove(min_item[1])
                break
            heapq.heappush(selected_scores, (min_item[0] + 1, min_item[1]))
            current_sum += 1
            max_median_score = max(max_median_score, selected_scores[0][0])
print(max_median_score)
