from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def make_keyboards(url):
    inline_kb1 = InlineKeyboardMarkup()
    button = InlineKeyboardButton('Высокое качество.', callback_data=f'hight|{url}')
    button2 = InlineKeyboardButton('Низкое качество.', callback_data=f'low|{url}')
    button3 = InlineKeyboardButton('Только аудио.', callback_data=f'audio|{url}')
    #button4 = InlineKeyboardButton('Отмена', callback_data=f'cancel')
    inline_kb1.add(button)
    inline_kb1.add(button2)
    inline_kb1.add(button3)
    #inline_kb1.add(button4)
    return inline_kb1