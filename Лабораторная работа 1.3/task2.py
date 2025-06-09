# TODO Напишите функцию find_common_participants

def find_common_participants(first_group, second_group, separator=','):
    first_group_list = set(first_group.split(separator))
    second_group_list = set(second_group.split(separator))
    common_participants = list(first_group_list.intersection(second_group_list))
    return sorted(common_participants)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

participants = find_common_participants(participants_first_group, participants_second_group, separator='|')
print('Общие участники:', participants)

# TODO Проверьте работу функции с разделителем отличным от запятой
