import requests
from abc import ABC, abstractmethod
import random


class MovieAPI(ABC):

    @abstractmethod
    def get_movie(self, keyword):  # function to get movie from API
        pass


class ImdbAPI(MovieAPI):

    def get_movie(self, keyword):
        url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/search/"
        headers = {
            'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
            'x-rapidapi-key': "982911d5fbmsh50e9a9eb143620ep1757b7jsn8ffa7604525f"
        }
        url_with_keyword = url + keyword
        response = requests.request("GET", url_with_keyword, headers=headers)
        print(response.content)
        movie = response.text
        return movie
