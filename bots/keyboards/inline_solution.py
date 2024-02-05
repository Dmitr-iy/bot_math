from aiogram.utils.keyboard import InlineKeyboardBuilder
from data.get_bd import execute_query


def get_solution(task_id, name_thems):
    builder = InlineKeyboardBuilder()

    query = ""
    params = ()
    num = [
        2, 4, 5,
        9, 12, 14,
        17, 19
    ]

    if task_id in num:
        query = "SELECT exercise_title FROM task_exercise WHERE task_id = %s"
        params = (task_id,)
    else:
        query = "SELECT e.title FROM exercise e JOIN thems_exercise te ON" \
                " e.title = te.exercise_title JOIN thems t ON te.thems_id = t.thems_id" \
                " WHERE t.name_thems = %s"
        params = (name_thems,)

    button_texts = execute_query(query, params)

    print("", button_texts)

    for button_text in button_texts:
        callback_data = f"solution:{task_id}:{button_text[0]}"
        builder.button(
            text=button_text[0],
            callback_data=callback_data,
        )

    builder.button(
        text='Назад',
        callback_data=f"solution:{task_id}:back",
    )

    if task_id == 9:
        builder.adjust(1, 2, 2)
    elif task_id == 19:
        builder.adjust(1, 1, 1, 1, 1)
    else:
        builder.adjust(1, 1, 1, 1, 1)

    return builder.as_markup()
