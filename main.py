from aiogram import *
from pytube import YouTube
import os
from keyboard import make_keyboards

def get_url(call):
    url = call.split('|')
    video_url = url[1]
    return video_url

token = '5817311405:AAHrpFa1GbXUUUD7kNbcEHOXR1rmnFNUreM'
bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start_message(message:types.Message):
    chat_id = message.chat.id
    message_text = 'Для скачивания видео отправь ссылку на Youtube'
    await bot.send_message(chat_id, message_text)


@dp.message_handler()
async def user_message(message:types.Message):
    chat_id = message.chat.id
    url = message.text
    yt = YouTube(url)
    if message.text.startswith == 'https://www.youtube.com/' or 'https://youtu.be/':
        message_text = f'Загрузка видео {yt.title} \nС канала {yt.author} будет начата после выбора качества'
        await bot.send_message(chat_id, message_text, reply_markup = make_keyboards(url))
        #await download_video(url, message, bot)


@dp.callback_query_handler()
async def handler_call(call: types.CallbackQuery):
    chat_id = call.from_user.id
    if call.data.startswith('low'):
        url = get_url(call.data)
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4')
        stream.get_lowest_resolution().download(f'{chat_id}', f'{chat_id}_{yt.title}')
        
    elif call.data.startswith('hight'):
        url = get_url(call.data)
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4')
        stream.get_highest_resolution().download(f'{chat_id}', f'{chat_id}_{yt.title}')
        
    path = f'{chat_id}' + os.sep + f'{chat_id}_{yt.title}'    
    with open(path, 'rb') as video:
        await bot.send_video(chat_id, video, caption="Загрузка завершена")
        os.remove(path)

# async def download_video(url, message, bot):
#     yt = YouTube(url)
#     stream = yt.streams.filter(progressive=True, file_extension='mp4')
#     stream.get_lowest_resolution().download(f'{message.chat.id}', f'{message.chat.id}_{yt.title}')
#     path = f'{message.chat.id}' + os.sep + f'{message.chat.id}_{yt.title}'
#     print(path)
#     with open(path, 'rb') as video:
#         await bot.send_video(message.chat.id, video, caption="Загрузка завершена")
#         os.remove(path)

if __name__ == '__main__':
    executor.start_polling(dp)