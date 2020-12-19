from misc import dp, bot
from aiogram.types import Message
from aiogram.types.message import ContentType
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
import logging

from .states import AdminState, ShowSearch, cancel_keyboard, admin_keyboard
from .menu import show_search
from user import get_all_users


@dp.message_handler(content_types = ContentType.ANY, state=AdminState.wait_message_text)
async def admin_send_message(message: Message, state: FSMContext):
    """
    Отправить сообщение всем пользователям.

    Parameters
    ----------
    message : Message
        Сообщение
    state : FSMContext
        Состояние админа
    """
    if message.text == 'Отмена':
        await AdminState.wait_admin_action.set()
        await message.answer('Выбери действие',
                             reply_markup=admin_keyboard)
    else:
        users = get_all_users()
        photo = message.photo
        video = message.video
        text = message.text
        for user in users:
            if photo:
                await bot.send_photo(user, photo[-1].file_id)
            if video:
                await bot.send_video(user, video.file_id)
            if text:
                await bot.send_message(user, text)


@dp.message_handler(state=AdminState.wait_admin_action)
async def admin_menu(message: Message, state: FSMContext):
    """
    Действия в меню для админа.

    Parameters
    ----------
    message : Message
        Сообщение
    state : FSMContext
        Состояние админа
    """
    import pdb; pdb.set_trace()
    if message.text == _('Send a message to everyone'):
        await AdminState.wait_message_text.set()
        await message.answer('Пришли сообщение, которое нужно всем разослать, если хочешь отменить, то нажми отмена.',
                             reply_markup=cancel_keyboard)
    if message.text == _('Text search'):
        await ShowSearch.waiting_for_search_text.set()
