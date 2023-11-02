import os
import dotenv
import logging


dotenv.load_dotenv()


API_TOKEN = os.getenv("API_TOKEN")
API_TOKEN_KINOPOISK = os.getenv("API_TOKEN_KINOPOISK")
API_TOKEN_GISMETEO = os.getenv("API_TOKEN_GISMETEO")
API_TOKEN_NASA = os.getenv("API_TOKEN_NASA")


logging.basicConfig(
    level=logging.INFO,
)
logger = logging.getLogger(__name__)
