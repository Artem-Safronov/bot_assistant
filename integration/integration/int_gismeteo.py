import logging
import settings
from integration.http_client import http_client
import pymorphy2
import re


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Gismeteo:

    def __init__(self, entities):
        self.url_geocoder = "http://api.openweathermap.org/geo/1.0/direct"
        self.url_gismeteo = "https://api.openweathermap.org/data/2.5/weather"
        self.api_key = settings.API_TOKEN_GISMETEO
        self.entities = entities

    async def main(self):
        city_name = self.entities.get('LOC')
        logger.info(f"City name: {city_name}")
        if city_name:
                try:
                    city_name = await self._to_nominative_case(city_name)
                    lat, lon = await self.get_geolocation(city_name)
                except Exception as e:
                    return [{"text": "Такого города не существует."}]
                integration_response = await self.get_weather(lat, lon)
                parse_response = await self._parse_response(integration_response)
                return parse_response
        return [{"text": "Какой город Вас интересует?"}]

    async def get_geolocation(self, location):
        params = {
            "q": location,
            "appid": self.api_key
        }
        response = await http_client(url=self.url_geocoder, params=params)
        for geolocation in response:
            lat = geolocation.get('lat')
            lon = geolocation.get('lon')
            logger.info(f"get_geolocation: {lat}, {lon}")
            return lat, lon

    async def get_weather(self, lat, lon):
        params = {
            "lat": lat,
            "lon": lon,
            "appid": self.api_key,
            "units": "metric",
            "lang": "ru"
        }
        response = await http_client(url=self.url_gismeteo, params=params)
        logger.info(f"get_weather: {response}")
        return response

    async def _parse_response(self, integration_response):
        name = integration_response.get('name')
        temp = integration_response.get('main').get('temp')
        description = integration_response.get('weather')[0].get('description')
        logger.info(f"Name: {name}, temp: {temp}, description: {description}")
        response_preparation = await self._response_preparation(name, temp, description)
        return [response_preparation]

    @staticmethod
    async def _response_preparation(name="-", temp="-", description="-"):
        text = f"В городе {name} на данный момент {description}. Температура воздуха {int(round(temp, 0))} ℃."
        return {"text": text}

    @staticmethod
    async def _to_nominative_case(city_name):
        morph = pymorphy2.MorphAnalyzer()
        parsed = morph.parse(city_name)[0]
        return parsed.inflect({'nomn'}).word
