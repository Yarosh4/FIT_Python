users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
dict = {
    "Общее количество" : 0,
    "Уникальные посещения" : 0
}
unique_users = set(users)
dict["Общее количество"] = len(users)
dict["Уникальные посещения"] = len(unique_users)
print(dict)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
