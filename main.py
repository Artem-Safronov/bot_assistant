import settings
from aiogram import Bot, Dispatcher, executor, types


bot = Bot(settings.API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def text(message: types.Message):
    pass


if __name__ == '__main__':
    executor.start_polling(dp)