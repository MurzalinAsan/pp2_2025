def is_highlyrated(movie):
    return movie["imdb"] > 5.5

movie_exmpl = { "name": "Dark Knight", "imdb": 9.0, "category": "Adventure" }
print(is_highlyrated(movie_exmpl))