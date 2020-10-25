from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup


class AdminState(StatesGroup):
    wait_admin_action = State()
    wait_message_text = State()


class ShowSearch(StatesGroup):
    waiting_for_search_text = State()


admin_keyboard = ReplyKeyboardMarkup(
    [['Поиск по тексту'], ['Отправить всем сообщение']], resize_keyboard=True
)
menu_keyboard = ReplyKeyboardMarkup(
    [['Поиск по тексту'], ['FAQ'], ['Помощь']], resize_keyboard=True
)
cancel_keyboard = ReplyKeyboardMarkup([['Отмена']], resize_keyboard=True)