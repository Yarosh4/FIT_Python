# TODO импортировать необходимые молули
import csv, json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    ...  # TODO считать содержимое csv файла
    with open(INPUT_FILENAME) as input:
        #десериализация из csv формата
        reader = csv.DictReader(input)
        #форматирование в список словарей
        data = [row for row in reader]

    ...  # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w') as output:
        #сереализация в json формат
        json.dump(data, output, indent=4)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
