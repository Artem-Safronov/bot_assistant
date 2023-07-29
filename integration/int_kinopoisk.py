import random
import logging
import settings
from integration.http_client import http_client


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Kinopoisk:

    def __init__(self, entities):
        self.url = "https://api.kinopoisk.dev/v1.3/movie"
        self.api_key = settings.API_TOKEN_KINOPOISK
        self.entities = entities

    async def main(self):
        integration_response = await self.get_data()
        parse_response = await self._parse_response(integration_response)
        return parse_response

    async def get_data(self):
        headers = {
            "accept": "application/json",
            "X-API-KEY": self.api_key,
        }
        params = {
            "limit": 100,
            "sortField": "rating.kp",
        }
        response = await http_client(url=self.url, headers=headers, params=params)
        return response

    async def _parse_response(self, integration_response):
        movies = integration_response.get("docs")
        three_random_movie = random.sample(movies, 3)
        list_movies = list()
        for movie in three_random_movie:
            name = movie.get("name")
            year = movie.get("year")
            genres = movie.get("genres")
            if genres:
                genres = genres[0].get("name")
            else:
                genres = "-"
            poster = movie.get("poster")
            if poster:
                poster = poster.get("url")
            response_preparation = await self._response_preparation(name, year, genres, poster)
            list_movies.append(response_preparation)
        logger.info(list_movies)

        return list_movies

    @staticmethod
    async def _response_preparation(name=None, year=None, genres=None, poster=None):
        text = f"Название: {name}\nГод выпуска: {year}\nЖанр: {genres}"
        return {"text": text, "poster": poster}
