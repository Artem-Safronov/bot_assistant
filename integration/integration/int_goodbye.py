import random


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
