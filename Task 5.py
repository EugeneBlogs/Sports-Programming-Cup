# ПРЕВЫШЕН ЛИМИТ ВРЕМЕНИ

n = int(input())

# Списки: [координата, тип события]
x_objects = []
y_objects = []

for _ in range(n):
    xa, ya, xb, yb = map(int, input().split())

    # Для оси X: отрезок от "min(xa, xb)" до "max(xa, xb)"
    x_objects.append([min(xa, xb), 1])  # Начало отрезка - "+1"
    x_objects.append([max(xa, xb) + 1, -1])  # Конец отрезка - "-1"

    # Аналогично для оси Y
    y_objects.append([min(ya, yb), 1])
    y_objects.append([max(ya, yb) + 1, -1])


# Сколько максимум отрезков пересекаются в одной точке
def count_max(objects):
    objects.sort()
    current = 0  # Текущее количество объектов в кадре
    best = 0  # Максимальное количество объектов в кадре

    # Обрабатываем все события
    for coord, delta in objects:
        current += delta
        best = max(best, current)
    return best


max_x = count_max(x_objects)
max_y = count_max(y_objects)
print(max(max_x, max_y))
