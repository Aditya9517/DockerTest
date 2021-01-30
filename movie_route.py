from flask import Flask, render_template
from movie_service import MovieService

app = Flask(__name__)


@app.route('/movie/<string:name>', methods=['GET'])
def movie_information(name):
    # Removing all the white spaces and putting the name together on the
    name = "".join(name.strip().split(' '))
    movie_review_url = MovieService().movie_information_service(name)

    return MovieService().movie_review_service(movie_review_url)


if __name__ == '__main__':
    app.run()

