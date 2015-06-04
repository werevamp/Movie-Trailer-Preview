"""This file holds the Movie class"""


class Movie(object):
    """Movie is a class that contains the attributes about Movie"""

    def __init__(self, movie_title, movie_storyline,
                 movie_poster, youtube_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = youtube_trailer
