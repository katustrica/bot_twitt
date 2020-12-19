from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup


class AdminState(StatesGroup):
    wait_admin_action = State()
    wait_message_text = State()


class ShowSearch(StatesGroup):
    waiting_for_search_text = State()


admin_keyboard = ReplyKeyboardMarkup(
    [[_('Text search')], [_('Send a message to everyone')]], resize_keyboard=True
)
menu_keyboard = ReplyKeyboardMarkup(
    [[_('Text search')], [_('FAQ')], [_('Help')]], resize_keyboard=True
)
cancel_keyboard = ReplyKeyboardMarkup([[_('Cancel')]], resize_keyboard=True)