from aiogram.utils.keyboard import InlineKeyboardBuilder
from data.get_bd import execute_query


def get_plan(title):
    builder = InlineKeyboardBuilder()

    query = "SELECT plan_solution FROM plan_title WHERE title = %s"
    params = (title,)
    texts = execute_query(query, params)

    print('', texts)

    for text in texts:
        truncated_text = text[0]

        print(truncated_text, truncated_text[:2])

        callback_data = f"{truncated_text}"
        builder.button(
            text=truncated_text,
            callback_data=callback_data,
        )

    return builder.as_markup()
