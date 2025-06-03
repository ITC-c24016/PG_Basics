import csv

character = [
    ["Top Gun", "Risky Business", "Minority Report"],
    ["Titanic", "The Revenant", "Inception"],
    ["Training Day", "Man on Fire", "Flight"]
]

with open("movies.csv", "w", newline="", encoding="utf-8") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=",")
    for movie_list in character:
        spamwriter.writerow(movie_list)


