import json
import csv

# Получение списка пользователей
with open("users.json") as users:
    full_users_list = json.load(users)

users_result = []
for j in full_users_list:
    dict_user = {}
    dict_user["name"] = j.get("name")
    dict_user["gender"] = j.get("gender")
    dict_user["address"] = j.get("address")
    dict_user["age"] = j.get("age")
    dict_user["books"] = []
    users_result.append(dict_user)


# Получение списка книг
with open("books.csv") as books:
    full_books = list(csv.DictReader(books))

books_result = []
for i in full_books:
    dict_books = {}
    dict_books['title'] = i.get('Title')
    dict_books['author'] = i.get('Author')
    dict_books['pages'] = int(i.get('Pages'))
    dict_books['genre'] = i.get('Genre')
    books_result.append(dict_books)


# Распределяем книги пользователям
for ind, book in enumerate(books_result):
    users_result[ind % len(users_result)]["books"].append(book)

# Записываем в json
with open("result.json", "w") as temp:
    json.dump(users_result, temp, indent=4)
