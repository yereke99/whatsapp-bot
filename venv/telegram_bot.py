from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, KeyboardButton, \
    InlineKeyboardMarkup
from logger import dp, bot
from text import text_start, text_else, text_photo, image, error
from keyboards import start_button
#from text_detection import recognition_text

from take_links import filter_links
from take_links import clients

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, text=text_start, reply_markup=start_button)


@dp.message_handler(content_types=['text'])
async def public(message: types.Message):
    m = message.text
    if (m == "Клиенттерді тексеру"):
        check = filter_links()
        await bot.send_message(message.from_user.id, text=check)
    elif (m == "Сумма"):
        cl = clients()
        await bot.send_message(message.from_user.id, text=cl)

    else:
        await bot.send_message(message.from_user.id, text=text_else)

'''
@dp.message_handler(content_types=['photo'])
async def photo_handle(message: types.photo_size):
    await message.photo[-1].download(image)
    data = recognition_text(image)
    # await bot.send_message(message.from_user.id, text=data)
    try:
        await bot.send_message(message.from_user.id, text=data)
    except Exception as e:
        await bot.send_message(message.from_user.id, text=error)

'''
