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

search = input("movie")
search = search.lower
def search():
    for movies in data:
        if search.lower() in movies['title'].lower():
            print(movies["title"])
        else:
            print("no movie")

search = input("genre")
search = search.lower
def genre():
    for movies in data:
        if search.lower() in movies["genre"].lower():
            print(movies["title"])
        else:
            print("no movies")
            
        




