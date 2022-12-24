from aiogram import *


token = '5817311405:AAHrpFa1GbXUUUD7kNbcEHOXR1rmnFNUreM'
bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_messsage(message:types.Message):
    chat_id = message.chat.id
    message_text = 'Для скачивания видео отправь ссылку на Youtube'
    await bot.send_message(chat_id, message_text)



if __name__ == '__main__':
    executor.start_polling(dp)