# TODO Напишите функцию find_common_participants

def find_common_participants(first_group, second_group, delimiter=','):
    result = []
    first = first_group.split(delimiter)
    second = second_group.split(delimiter)
    for i in first:
        for j in second:
            if i.__eq__(j):
                result.append(i)
    result.sort()
    return result



delimiter = "|"
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, delimiter))
# TODO Провеьте работу функции с разделителем отличным от запятой
