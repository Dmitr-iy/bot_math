from aiogram.utils.keyboard import InlineKeyboardBuilder
from bots.utils.callbackdata import SelectTem
from data.get_bd import execute_query


def get_tem_task(task_id):
    builder = InlineKeyboardBuilder()

    query = "SELECT thems FROM task_thems WHERE task_id = %s"
    params = (task_id,)
    button_texts = execute_query(query, params)

    print("", button_texts)

    for button_text in button_texts:

        builder.button(
            text=button_text[0],
            callback_data=SelectTem(task_id=task_id, tem_name=str(button_text[0]), back=str()),
        )

    builder.button(
        text='🔙',
        callback_data=SelectTem(task_id=task_id, tem_name=str(), back='back'),
    )

    builder.adjust(1, 1, 1, 1, 1)

    # if task_id in [1, 6, 7, 16]:
    #     builder.adjust(2, 1)
    # elif task_id == 3:
    #     builder.adjust(1, 2, 2)
    # elif task_id == 10:
    #     builder.adjust(2, 2, 1, 1)
    # elif task_id in [11, 13, 15, 18]:
    #     builder.adjust(1, 1)

    return builder.as_markup()
