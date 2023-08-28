from integration.integration.int_citations import Сitations
from integration.integration.int_kinopoisk import Kinopoisk
from integration.integration.int_gismeteo import Gismeteo
from integration.integration.int_greeting import Greeting
from integration.integration.int_goodbye import Goodbye
from integration.integration.int_global import Global
from integration.integration.int_nasa import Nasa


INTEGRATION_CLASSES = {
    "kinopoisk": Kinopoisk,
    "weather": Gismeteo,
    "greeting": Greeting,
    "goodbye": Goodbye,
    "global": Global,
    "citations": Сitations,
    "nasa": Nasa,
}
