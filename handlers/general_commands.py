from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from misc import bot, dp, admin_ids
from user import User, get_all_users, set_all_users
import logging
from .menu import menu_keyboard
from .states import AdminState, admin_keyboard

@dp.message_handler(commands='cancel', state='*')
@dp.message_handler(Text(equals='Отмена', ignore_case=True), state='*')
async def cmd_cancel(message: types.Message, state: FSMContext):
    """
    Обработчик кнопки Отмена.

    Parameters
    ----------
    message : types.Message
        Текст сообщения (Отмена)
    state : FSMContext
        Сброс состояния пользователя.
    """

    await state.finish()
    await message.answer('Выбрете действие:',
                            reply_markup=menu_keyboard)


@dp.message_handler(commands=['start'], state='*')
async def cmd_start(message: types.Message):
    """
    Обработчик кнопки старт. Определяет от кого пришло сообщение.

    Parameters
    ----------
    message : types.Message
        Текст сообщения
    """
    if message.from_user.id in admin_ids:
        await message.answer('Привет, ты админ, что хочешь делать?',
                             reply_markup=admin_keyboard)
        await AdminState.wait_admin_action.set()
    else:
        all_users = get_all_users()
        if message.from_user.id not in all_users:
            all_users[message.from_user.id] = User(message.from_user.full_name, message.from_user.id)
            set_all_users(list(all_users.values()))
            for id in admin_ids:
                new_user_msg = (
                    f'Новый пользователь {message.from_user.full_name} .'
                    f'Всего пользователей {len(all_users)}'
                )
                await bot.send_message(id, new_user_msg)
                logging.info(new_user_msg)
                await message.answer('Привет, друг, я такой-то бот, умею вот это:\n1) ---\n 2) ...',
                                     reply_markup=menu_keyboard)
