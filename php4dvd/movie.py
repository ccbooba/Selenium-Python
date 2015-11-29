class Movie(object):

    def __init__(self, movie_name=None):
        self.movie_name = movie_name

    @classmethod
    def Movie_first(cls):
        return cls(movie_name="Movie #1")
