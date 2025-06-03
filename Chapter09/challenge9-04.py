import csv

character = [
    ["トップガン", "リスキービジネス", "マイノリティ・リポート"],
    ["タイタニック", "レヴェナント", "インセプション"],
    ["トレーニング・デイ", "マン・オン・ファイア", "フライト"]
]

with open("movies_jp.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    for movie_list in character:
        writer.writerow(movie_list)

