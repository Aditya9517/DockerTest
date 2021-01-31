from flask import Flask, render_template
from movie_service import MovieService

app = Flask(__name__)


@app.route('/movie/url/<string:name>', methods=['GET'])
def movie_information(name):
    return MovieService().movie_information_service(name)

@app.route('/movie/review/<string:name>', methods=['GET'])
def movie_review(name):
    return MovieService().movie_review_service(
        MovieService().movie_information_service(name)
    )


if __name__ == '__main__':
    app.run()

