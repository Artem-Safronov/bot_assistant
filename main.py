import logging
import settings
from aiogram import Bot, Dispatcher, executor, types
from classifier.trained_classifier import trained_classifier
from classifier.text_classification import text_classification
from integration.base_integration import base_integration


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(settings.API_TOKEN)
dp = Dispatcher(bot)
classifier, vectorizer = None, None


@dp.message_handler()
async def mes(message: types.Message):
    logging.info(f"received message: {message}")
    intent = await text_classification(message.text, classifier, vectorizer)
    logger.info(intent)
    response = await base_integration(intent)
    for res in response:
        text = res.get('text')
        poster = res.get('poster')
        if poster:
            await bot.send_photo(message.chat.id, photo=poster, caption=text)
        else:
            await message.answer(text)


if __name__ == '__main__':
    classifier, vectorizer = trained_classifier()
    executor.start_polling(dp)
