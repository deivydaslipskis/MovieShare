from flask import Flask, request
from movie_api import movie_api

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/getmovie')
def get_movie_title():
    keyword = request.args.get('keyword')
    movie_title = search_movie_in_api(keyword)
    return movie_title


def search_movie_in_api(keyword):
    api = movie_api.ImdbAPI()
    movie_from_api = api.get_movie(keyword=keyword)
    if movie_from_api is not None:
        return movie_from_api


if __name__ == "__main__":
    app.run(debug=True)
