import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

"""for index, item in enumerate(data):
    print(item["title"])"""

year = 0
movies = []
while data["year"]:
    year == input("Select a year to get all movies after that year")    
    if data["year"] > year:
        movies.append (data["title"])
    print(movies)



movies = []
while data["year"]:
    years = (x, y)
    years == (input(years)) 
    if data["year"] > x and data["year"] < y:
        movies.append (data["title"])
    print(movies)

year = 0
movies = []
while data["year"]:
    year == input("Select a year")
if data["year"] == year:
    movies.append(data["title"])
    print(movies)

def search():




def genre():
    genre = input("Pick a genre")
    movies = []
    while data["genre"]:
        if data["genre"] == genre:
            movies.append (data["title"])
            print(movies)


    