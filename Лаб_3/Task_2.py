# TODO Напишите функцию find_common_participants
def find_common_participants(a, b, list_=[]):
    list_ = sorted(a.intersection(b))
    return print(list_)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

first_group = set(participants_first_group.split('|'))
second_group = set(participants_second_group.split('|'))
common_participants = []

find_common_participants(first_group, second_group, common_participants)

# TODO Провеьте работу функции с разделителем отличным от запятой
