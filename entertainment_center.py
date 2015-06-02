#!/usr/bin/python
"""Entertainement center populates the app with movies and runs the open movies
page to generate the HTML"""

import fresh_tomatoes
import media

def populate_movie_details():
    """populate movie details generates a list of movies and outputs
    the movie objects into an array"""

    toy_story = media.Movie(
        "Toy story",
        "A story of a boy and his toys",
        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
        "https://www.youtube.com/watch?v=KYz2wyBy3kc"
    )

    avatar = media.Movie(
        "Avatar",
        "A marine on an alien planet",
        "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
        "https://www.youtube.com/watch?v=d1_JBMrrYw8"
    )

    sup = media.Movie(
        "Up",
        "A house lifted by baloons",
        "http://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",
        "https://www.youtube.com/watch?v=pkqzFUhGPJg"
    )

    interstellar = media.Movie(
        "Interstellar",
        "Finding new life in space",
        "http://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
        "https://www.youtube.com/watch?v=nyc6RJEEe0U"
    )

    big_hero_6 = media.Movie(
        "Big Hero 6",
        "Boy genius builds robots and saves world",
        "http://upload.wikimedia.org/wikipedia/en/4/4b/Big_Hero_6_%28film%29_poster.jpg",
        "https://www.youtube.com/watch?v=8IdMPpKMdcc"
    )

    the_lego_movie = media.Movie(
        "The Lego Movie",
        "Everything is awesome, Everything is cool when you're part of a team!",
        "http://upload.wikimedia.org/wikipedia/en/1/10/The_Lego_Movie_poster.jpg",
        "https://www.youtube.com/watch?v=fZ_JOBCLF-I"
    )

    movies = [toy_story, avatar, sup, interstellar, big_hero_6, the_lego_movie]

    return movies

MOVIES = populate_movie_details()

fresh_tomatoes.open_movies_page(MOVIES)
