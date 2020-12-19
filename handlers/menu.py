from misc import dp, admin_ids, config
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
import logging
from user import MessageSchema
from requests import get
from marshmallow.utils import EXCLUDE

from .states import AdminState, ShowSearch, menu_keyboard, cancel_keyboard, admin_keyboard

LIMIT = 20

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
    if (text := message.text) == 'Отмена':
        if message.from_user.id in admin_ids:
            await AdminState.wait_admin_action.set()
            await message.answer(text='Выбери действие:', reply_markup=admin_keyboard)
        else:
            await state.finish()
            await message.answer('Привет, что хочешь делать?',
                                 reply_markup=menu_keyboard)
    else:
        ip = config['server']['ip']
        port = config['server']['port']
        response = get(f'http://{ip}:{port}/?request={text}&limit={LIMIT}')
        if response.status_code == 200:
            messages = "\n--------------\n".join(
                MessageSchema(many=True, unknown=EXCLUDE).loads(response.text, partial=True)
            )
        else:
            messages = response.text

        if len(messages) > (chunk := 4096):
            for x in range(0, len(messages), chunk):
                await message.answer(messages[x:x+chunk])
        else:
            await message.answer(messages)

