class Movie(object):

    def __init__(self, movie_name=None, year=None, notes=None):
        self.movie_name = movie_name
        self.year = year
        self.notes = notes

    @classmethod
    def Movie_first(cls):
        """ This movie will be added with success """
        return cls(movie_name="Movie #111", year="2014", notes="Worth seeing, sure!")

    @classmethod
    def Movie_second(cls):
        """ This movie will fail to be added, as Year is blank """
        return cls(movie_name="Movie #222", year="", notes="333")