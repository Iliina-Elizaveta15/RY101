def find_common_participants(group1, group2, delimiter="|"):

    participants1 = set(group1.split(delimiter))
    participants2 = set(group2.split(delimiter))
    common_participants = participants1.intersection(participants2)
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


common_participants = find_common_participants(participants_first_group, participants_second_group)
print(f"Общие участники: {', '.join(common_participants)}")