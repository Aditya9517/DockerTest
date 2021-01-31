from movie_repository import MovieRepository


class MovieService:

    def movie_information_service(self, name):
        # Removing all the white spaces and putting the name together on the
        name = "".join(name.strip().split(' '))
        return MovieRepository().movie_information_repository(name)

    def movie_review_service(self, name):
        return MovieRepository().movie_reviews(name)
