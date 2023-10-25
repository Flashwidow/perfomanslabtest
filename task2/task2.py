import sys
import math

# Функция для определения положения точки относительно окружности
def point_position(point, circle_center, radius):
    distance = math.sqrt((point[0] - circle_center[0]) ** 2 + (point[1] - circle_center[1]) ** 2)
    if math.isclose(distance, radius, rel_tol=1e-9):
        return 0  # Точка лежит на окружности
    elif distance < radius:
        return 1  # Точка внутри окружности
    else:
        return 2  # Точка снаружи окружности

# Проверка наличия аргументов командной строки
if len(sys.argv) != 3:
    print("Использование: python3 task2.py circle.txt dot.txt")
    sys.exit(1)

# Считываем координаты центра окружности и радиус
with open(sys.argv[1], 'r') as file1:
    circle_coords = list(map(float, file1.readline().split()))
    circle_radius = float(file1.readline())

# Считываем координаты точек и определяем их положение относительно окружности
with open(sys.argv[2], 'r') as file2:
    for line in file2:
        point_coords = list(map(float, line.split()))
        position = point_position(point_coords, circle_coords, circle_radius)
        print(position)

