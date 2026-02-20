import json
import csv

# Получение списка пользователей
with open("users.json") as spi:
    full_users = json.load(spi)

users_result = []
for j in full_users:
    newslo_user = {}
    newslo_user["name"] = j["name"]
    newslo_user["gender"] = j["gender"]
    newslo_user["address"] = j["address"]
    newslo_user["age"] = j["age"]
    newslo_user["books"] = []
    users_result.append(newslo_user)


# Получение списка книг
with open("books.csv") as opp:
    full_books = list(csv.DictReader(opp))

books_result = []
for i in full_books:
    temp_slo_books = {}
    temp_slo_books['title'] = i['Title']
    temp_slo_books['author'] = i['Author']
    temp_slo_books['pages'] = int(i['Pages'])
    temp_slo_books['genre'] = i['Genre']
    books_result.append(temp_slo_books)


# Распределяем книги пользователям
for p in range(len(books_result)):
    users_result[p % len(users_result)]["books"].append(books_result[p])


# Записываем в json
with open("result.json", "w") as temp:
    json.dump(users_result, temp, indent=4)
