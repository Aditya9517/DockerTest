from movie_repository import MovieRepository


class MovieService:

    def movie_information_service(self, name):
        return MovieRepository().movie_information_repository(name)
