import random


class Greeting:

    def __init__(self, entities):
        self.answers = (
            "Привет, чем Вам помочь?",
            "Приветствую!",
            "Добро пожаловать!",
        )

    async def main(self):
        response = random.choice(self.answers)
        return [{"text": response}]
