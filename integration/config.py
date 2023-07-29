from integration.int_kinopoisk import Kinopoisk
from integration.int_gismeteo import Gismeteo


INTEGRATION_CLASSES = {
    "kinopoisk": Kinopoisk,
    "weather": Gismeteo,
}
