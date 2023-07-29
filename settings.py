import os
import dotenv


dotenv.load_dotenv()


API_TOKEN = os.getenv("API_TOKEN")
API_TOKEN_KINOPOISK = os.getenv("API_TOKEN_KINOPOISK")
API_TOKEN_GISMETEO = os.getenv("API_TOKEN_GISMETEO")