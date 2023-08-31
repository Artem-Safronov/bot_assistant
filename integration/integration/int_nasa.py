import logging
import settings
from integration.http_client import http_client


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Nasa:

    def __init__(self, entities):
        self.url = "https://api.nasa.gov/planetary/apod"
        self.api_key = settings.API_TOKEN_NASA

    async def main(self):
        integration_response = await self.get_data()
        if not integration_response:
            return [{"text": "Получение фотографии космоса временно не доступно."}]
        response_preparation = await self._response_preparation(integration_response)
        logger.info(f"nasa integration response: {integration_response}")
        return response_preparation

    async def get_data(self):
        params = {
            "api_key": self.api_key
        }
        response = await http_client(url=self.url, params=params)
        return response

    @staticmethod
    async def _response_preparation(integration_response):
        text = integration_response.get('title')
        poster = integration_response.get('url')
        return [{"text": text, "poster": poster}]
