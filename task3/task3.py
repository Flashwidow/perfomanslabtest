import json
import sys

def fill_values(tests, values):
    def update_values(test, values):
        if "values" in test:
            test["value"] = "failed"
            for subtest in test["values"]:
                update_values(subtest, values)
            for value in values:
                if value["id"] == test["id"]:
                    test["value"] = value["value"]
                    break
        else:
            for value in values:
                if value["id"] == test["id"]:
                    test["value"] = value["value"]
                    break

    # Обходим список тестов и обновляем их значения            
    for test in tests:
        update_values(test, values)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python3 task3.py tests.json values.json")
        sys.exit(1)
    tests_file_name = sys.argv[1]
    values_file_name = sys.argv[2]
    # Открываем и читаем JSON-файлы
    with open(tests_file_name, "r") as tests_file, open(values_file_name, "r") as values_file:
        tests_data = json.load(tests_file)
        values_data = json.load(values_file)

    
    # Вызываем функцию fill_values для обновления значений тестов
    fill_values(tests_data["tests"], values_data["values"])

    # Сохраняем обновленные данные в файл отчета
    with open("report.json", "w") as report_file:
        json.dump(tests_data, report_file, indent=2)






