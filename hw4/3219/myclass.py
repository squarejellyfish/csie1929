from collections import OrderedDict

class Movie:
    def __init__(self, name, year, director) -> None:
        self.name = name
        self.year = year
        self.director = director
        self.metadata = OrderedDict()

    def __str__(self) -> str:
        return self.name

    def show_info(self):
        print("Movie_name: {}".format(self.name))
        print("Year: {}".format(self.year))
        print("Director: {}".format(self.director))

        for tag, value in self.metadata.items():
            print("{} : {}".format(tag, value))

    def add_metadata(self, tag, value):
        self.metadata[tag] = value

class Database:
    def __init__(self, *Movie) -> None:
        self.movies = list()
        self.movies.extend(Movie)

    def add(self, Movie):
        self.movies.append(Movie)

    def list_movie(self):
        print("There are {} movies in Database".format(len(self.movies)))
        for movie in self.movies:
            movie.show_info()
            print()
