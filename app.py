import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

for index, item in enumerate(data):
    print(item["title"])

"""year = int(input("Pick a year to get movies made after that year."))
for movies in data:
    if movies["year"] > year:
        print(movies["title"])"""


"""year = int(input("pick a year to get all movies made after that year"))
yeartwo = int(input("pick a year to get all movies made before that year"))
for movies in data:
    if movies["year"] > year and movies["year"] < yeartwo:
        print(movies["title"])"""

"""year = int(input("pick a year to get all movies made during that year"))
for movies in data:
    if movies["year"] == year:
        print(movies["title"])"""

"""
def movie():
    search = input("movie").lower()
    found = False
    for movie in data:
        if search in movie["title"].lower():
            print(movie["title"])
            found = True
    if found == False:
        print("No movie found.")
movie()
"""
"""
def genre():
    search = input("genre").lower()
    found = False
    for movie in data:
        if search in movie["genre"].lower():
            print(movie["title"])
            found = True
    if found == False:
        print("No movies found in that genre.")
genre()
"""

        




