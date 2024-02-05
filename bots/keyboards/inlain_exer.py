from aiogram.utils.keyboard import InlineKeyboardBuilder
from bots.utils.callbackdata import SelectExercises
from data.get_bd import execute_query


def get_exercises(solution):
    builder = InlineKeyboardBuilder()

    query = "SELECT sol_plan_title FROM plan_title WHERE plan_solution = %s"
    params = (solution,)
    texts = execute_query(query, params)
    print(texts)
    for text in texts:
        tex = str(text[0])
        print(tex)
        callback_data = SelectExercises(solution=tex, back='back')
        builder.button(
            text=tex,
            callback_data=callback_data,
        )

    builder.button(
        text='Назад',
        callback_data=SelectExercises(solution='back', back='back'),
    )
    return builder.as_markup()
