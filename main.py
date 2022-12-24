from aiogram import *
from pytube import YouTube
import os

token = '5817311405:AAHrpFa1GbXUUUD7kNbcEHOXR1rmnFNUreM'
bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_messsage(message:types.Message):
    chat_id = message.chat.id
    message_text = 'Для скачивания видео отправь ссылку на Youtube'
    await bot.send_message(chat_id, message_text)


@dp.message_handler()
async def user_message(message:types.Message):
    chat_id = message.chat.id
    url = message.text
    yt = YouTube(url)
    if message.text.startswith == 'https://www.youtube.com/' or 'https://youtu.be/':
        message_text = f'Загрузка видео начата {yt.title} \nС канала {yt.author}'
        await bot.send_message(chat_id, message_text)
        await download_video(url, message, bot)
        
async def download_video(url, message, bot):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4')
    stream.get_lowest_resolution().download(f'{message.chat.id}', f'{message.chat.id}_{yt.title}')
    path = f'{message.chat.id}/{message.chat.id}_{yt.title}'
    with open(path, 'rb') as video:
        await bot.send_video(message.chat.id, video, caption="Загрузка завершена")
        os.remove(path)

if __name__ == '__main__':
    executor.start_polling(dp)