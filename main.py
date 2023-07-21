import settings
from aiogram import Bot, Dispatcher, executor, types
from classifier.trained_classifier import trained_classifier


bot = Bot(settings.API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def text(message: types.Message):
    pass


if __name__ == '__main__':
    trained_classifier()
    executor.start_polling(dp)