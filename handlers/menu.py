from misc import dp, admin_ids
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
import logging

from .states import AdminState, ShowSearch, menu_keyboard, cancel_keyboard, admin_keyboard



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
    await ShowSearch.waiting_for_search_text.set()
    await message.answer('Введи поисковой запрос!', reply_markup=cancel_keyboard)


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
        if message.from_user.id in admin_ids:
            await AdminState.wait_admin_action.set()
            await message.answer(text='Выбери действие:', reply_markup=admin_keyboard)
        else:
            await state.finish()
            await message.answer('Привет, что хочешь делать?',
                                reply_markup=menu_keyboard)
    else:
        await message.answer('Ничего не нашел, потому что пока ничего у меня нет из функционала :-)')

