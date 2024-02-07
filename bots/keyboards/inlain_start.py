from aiogram.utils.keyboard import InlineKeyboardBuilder
from bots.utils.callbackdata import SelectStart


def get_start_task():
    builder = InlineKeyboardBuilder()

    builder.button(
        text='\U0001F4DA Начать \U0001F4C8',
        callback_data=SelectStart(task_id=0)
    )

    return builder.as_markup()
