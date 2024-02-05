from aiogram.utils.keyboard import InlineKeyboardBuilder
from bots.utils.callbackdata import SelectFinish


def get_finish():
    builder = InlineKeyboardBuilder()

    builder.button(
        text="VK",
        url="https://vk.com/koshelevgeniya"
    )
    builder.button(
        text="контакт Telegram",
        url="https://t.me/evgeniyaKoshel"
    )

    builder.button(
        text='К Заданиям',
        callback_data=SelectFinish(back='back', support='back'),
    )

    builder.button(
        text='support',
        callback_data=SelectFinish(back='support', support='support'),
    )

    builder.adjust(2, 2)

    return builder.as_markup()
