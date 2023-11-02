from settings import API_TOKEN, logger
from aiogram import Bot, Dispatcher, executor, types
from classifier.trained_classifier import trained_classifier
from classifier.text_classification import text_classification
from integration.base_integration import base_integration
from db.db import Context, db_main
import sqlalchemy
import asyncio


bot = Bot(API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    logger.info(f"received message: {message}")
    text = "Добрый день! Я — виртуальный ассистент «Савелий»."
    await message.answer(text)


@dp.message_handler(content_types=['photo'])
async def photo(message: types.Message):
    text = "Я еще не умею работать с картинками."
    await message.answer(text)


@dp.message_handler()
async def mes(message: types.Message):
    logger.info(f"received message: {message}")
    id_user = message["from"]["id"]
    context = await db_client.fetch(sqlalchemy.text(f"SELECT * FROM context WHERE id_user = {id_user} ORDER BY id DESC"))
    logger.info(f"Context: {context}")
    intent, entities = await text_classification(message.text, classifier, vectorizer, context)
    logger.info(intent)
    response = await base_integration(intent, entities)
    logger.info(response)
    for res in response:
        text = res.get('text')
        poster = res.get('poster')
        if poster:
            await bot.send_photo(message.chat.id, photo=poster, caption=text)
        else:
            await message.answer(text)
    await db_client.add(Context(id_user=id_user, data={"intent": intent, "entities": entities}))


if __name__ == '__main__':
    classifier, vectorizer = trained_classifier()
    loop = asyncio.get_event_loop()
    db_client = loop.run_until_complete(db_main())
    executor.start_polling(dp, loop=loop)
