from flask import Flask
from movie_service import MovieService

app = Flask(__name__)


@app.route('/movie/<string:name>', methods=['GET'])
def movie_information(name):
    # Removing all the white spaces and putting the name together on the
    name = "".join(name.strip().split(' '))
    return MovieService().movie_information_service(name)


if __name__ == '__main__':
    app.run()

