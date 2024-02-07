from aiogram.utils.keyboard import InlineKeyboardBuilder
from bots.utils.callbackdata import SelectFinish


def get_finish(task_id, name_them):
    print("Task Finished:", task_id)
    print("Finish thems:", name_them)

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
        text='↩ К Задачам',
        callback_data=SelectFinish(back=name_them, task_id=task_id),
    )

    builder.button(
        text='↩ К Заданиям',
        callback_data=SelectFinish(back='back', task_id=task_id),
    )

    builder.button(
        text='⚙ support 🛠',
        callback_data=SelectFinish(back='support', task_id=task_id),
    )

    builder.adjust(2, 2)

    return builder.as_markup()
