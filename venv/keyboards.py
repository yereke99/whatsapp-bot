from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, KeyboardButton, \
    InlineKeyboardMarkup
import telegram_bot
from logger import dp, bot
from aiogram import types

#
send_list_of_clients = KeyboardButton('Сумма')
send_check = KeyboardButton('Клиенттерді тексеру')
start_button = ReplyKeyboardMarkup().row(send_check, send_list_of_clients)
# start_button = ReplyKeyboardMarkup().row(send_list_of_clients)
#

send_list_of_clients = KeyboardButton('Клиенттер тізімі')


