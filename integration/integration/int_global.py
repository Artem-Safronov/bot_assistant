import random


class Global:

    def __init__(self, entities):
        self.answers = (
            "Я пока не знаю, что с этим делать.",
        )

    async def main(self):
        response = random.choice(self.answers)
        return [{"text": response}]
