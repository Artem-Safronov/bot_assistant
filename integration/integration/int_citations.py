import logging
from integration.http_client import http_client


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Сitations:

    def __init__(self, entities):
        self.url = "http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=ru"

    async def main(self):
        integration_response = await self.get_data()
        response_preparation = await self._response_preparation(integration_response)
        logger.info(f"forismatic integration response: {integration_response}")
        return response_preparation

    async def get_data(self):
        response = await http_client(url=self.url)
        return response

    @staticmethod
    async def _response_preparation(integration_response):
        text = integration_response.get('quoteText')
        return [{"text": text}]
