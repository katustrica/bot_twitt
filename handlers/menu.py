from misc import dp
from aiogram.types import ReplyKeyboardMarkup, Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
import logging


class ShowSearch(StatesGroup):
    waiting_for_search_text = State()


menu_keyboard = ReplyKeyboardMarkup(
    [['Поиск по тексту'], ['FAQ'], ['Помощь']], resize_keyboard=True
)

@dp.message_handler(Text(equals='FAQ', ignore_case=True), state='*')
async def show_faq(message: Message):
    """
    Открывает faq.

    Parameters
    ----------
    message : Message
        Текст сообщения
    """
    await message.answer('^_^')


@dp.message_handler(Text(equals='Помощь', ignore_case=True), state='*')
async def show_help(message: Message):
    """
    Открывает помощь

    Parameters
    ----------
    message : Message
        Текст сообщения
    """
    await message.answer('0_0')


@dp.message_handler(Text(equals='Поиск по тексту', ignore_case=True), state='*')
async def show_search(message: Message):
    """
    Показывает пользователю меню.

    Parameters
    ----------
    message : Message
        Текст сообщения
    state : FSMContext
        Сброс состояния пользователя.
    """
    keyboard = ReplyKeyboardMarkup([['Отмена']], resize_keyboard=True)
    await ShowSearch.waiting_for_search_text.set()
    await message.answer('Введи поисковой запрос!', reply_markup=keyboard)


@dp.message_handler(state=ShowSearch.waiting_for_search_text)
async def search(message: Message, state: FSMContext):
    """
    Показывает пользователю меню.

    Parameters
    ----------
    message : Message
        Текст сообщения
    state : FSMContext
        Сброс состояния пользователя.
    """
    if message.text == 'Отмена':
        await state.finish()
        await message.answer('Привет, что хочешь делать?',
                             reply_markup=menu_keyboard)
    else:
        await message.answer('Ничего не нашел, потому что пока ничего у меня нет из функционала :-)')

