from aiogram.utils.keyboard import InlineKeyboardBuilder
from bots.utils.callbackdata import TaskInfo


def get_num_task():
    builder = InlineKeyboardBuilder()

    for task_id in range(1, 21):
        if task_id == 20:
            button_text = "задания которые были в ЕГЭ 2023"
        else:
            button_text = str(task_id)

        builder.button(text=button_text, callback_data=TaskInfo(
            task_id=task_id, tem=str(task_id)))

    builder.adjust(4, 4, 4, 4, 3)
    return builder.as_markup()
