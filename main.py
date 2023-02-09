import requests
from bs4 import BeautifulSoup
# import lxml  # Used for initial import

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
web = response.text

soup = BeautifulSoup(web, "html.parser")

movie_list = [film.get_text() for film in soup.find_all(name="h3", class_="title")]
movie_list.reverse()
print(movie_list)

with open("movies.txt", "a", encoding="latin-1") as file:
    for film in movie_list:
        number = film.split(" ")[0]
        film_name = " ".join(film.split()[1:])
        file.write(f"{number} {film_name}\n")
