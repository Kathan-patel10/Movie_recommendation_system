import requests


def fetch_poster(movie_title):
    url = "http://www.omdbapi.com/?t={}&apikey=4a8eb2f2".format(movie_title)
    data = requests.get(url)
    data = data.json()
    poster_path = data['Poster']
    full_path = poster_path
    print(full_path)
    return full_path

fetch_poster('Avatar')