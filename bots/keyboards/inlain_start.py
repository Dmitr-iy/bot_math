from aiogram.utils.keyboard import InlineKeyboardBuilder
from bots.utils.callbackdata import SelectStart


def get_start_task():
    builder = InlineKeyboardBuilder()

    builder.button(
        text='Начать',
        callback_data=SelectStart(task_id=0)
    )

    return builder.as_markup()
