import sys

def circular_array_path(n, m):
    result = [] # Создаем пустой список для хранения пути
    i = 1
    while True:
        result.append(i) # Добавляем текущую позицию в список пути
        i = 1 + (i + m - 2) % n # Вычисляем следующую позицию в массиве
        if i == 1:
            break
    return result

if __name__ == '__main__':
    n = int(sys.argv[1])
    m = int(sys.argv[2])
  
    result = circular_array_path(n, m)
    result_str = ''.join(map(str, result)) # Преобразуем список пути в строку
    print(result_str)

