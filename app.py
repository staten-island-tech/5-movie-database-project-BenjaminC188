import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

"""for index, item in enumerate(data):
    print(item["title"])"""

year = 0
while data:
    if year == input("select a year to get all movies made after that year."):
        year > data["year"]
        print(data["title"])