from aiogram.utils.keyboard import InlineKeyboardBuilder
from bots.utils.callbackdata import SelectPlan
from data.get_bd import execute_query


def get_plan(title):
    builder = InlineKeyboardBuilder()

    query = "SELECT plan_solution FROM plan_title WHERE title = %s"
    params = (title,)
    texts = execute_query(query, params)

    print('', texts)

    for text in texts:
        truncated_text = str(text[0])

        print(truncated_text)

        callback_data = SelectPlan(title=truncated_text, back='back')
        builder.button(
            text=truncated_text,
            callback_data=callback_data,
        )

        builder.button(
            text='Назад',
            callback_data=SelectPlan(title='back', back='back')
        )

    return builder.as_markup()
