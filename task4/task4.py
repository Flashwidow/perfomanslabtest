import sys

# Функция для чтения чисел из файла и сохранения их в список
def read_numbers(filename):
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers

# Функция для вычисления минимального количества ходов
def min_moves_to_equalize(numbers: list):
    # Сортируем числа для удобства
    numbers.sort()
    # Вычисляем медиану списка
    median = numbers[len(numbers) // 2]
    # Вычисляем сумму абсолютных разностей между каждым числом и медианой
    moves = sum(abs(num - median) for num in numbers)
    return moves

if len(sys.argv) != 2:
    print("Пожалуйста, укажите имя файла в качестве аргумента командной строки.")
else:
    filename = sys.argv[1]
    numbers = read_numbers(filename)
    moves = min_moves_to_equalize(numbers)
    print(moves)
