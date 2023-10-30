users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
Len_users = len(users)
unique_users = set(users)
count_unique_users = len(unique_users)
Statistics_dict = {
    "Общее количество": Len_users,
    "Уникальные посещения": count_unique_users
}
print(Statistics_dict)
