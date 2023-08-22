from aiogram import *
from database import DataBase
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os


TOKEN = "5551196958:AAEH4sgnRWxHUxY5qshSM0huiyFUg9Hpo8k"
code_admin = 274139796

inst_ = {
    1: "ИРИТ–РтФ",
    2: "ИНМИТ",
    3: "УРАЛЭНИН",
    4: "ФТИ",
    5: "ИСА",
    6: "УГИ",
    7: "ИФКСиМП",
    8: "ИЕНиМ",
    9: "ИНЭУ",
    10: "ХТИ"
}

want_ = {
    1: "Друг 😝",
    2: "Подруга 💅",
    3: "Парень 🏄‍",
    4: "Девушка 💃"
}

sex_ = {
    1: "Мальчик 👦",
    0: "Девочка 👧"
}
