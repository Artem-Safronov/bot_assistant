import logging
import random


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Goodbye:

    def __init__(self, entities):
        self.answers = (
            "До свидания!",
            "Всего хорошего!",
            "Пока!",
            "Удачи!",
        )

    async def main(self):
        response = random.choice(self.answers)
        return [{"text": response}]
