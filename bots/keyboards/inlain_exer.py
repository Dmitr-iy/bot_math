from aiogram.utils.keyboard import InlineKeyboardBuilder
from bots.utils.callbackdata import SelectExercises
from data.get_bd import execute_query


def get_exercises(solution, task_id, them):
    print("Solution:", solution)
    print("Task EXER:", task_id)
    print("Them EXER:", them)
    builder = InlineKeyboardBuilder()

    query = "SELECT sol_plan_title FROM plan_title WHERE plan_solution = %s"
    params = (solution,)
    texts = execute_query(query, params)
    print(texts)

    for text in texts:
        tex = str(text[0])
        print(tex)
        callback_data = SelectExercises(solution=tex, them=them, task_id=task_id)
        builder.button(
            text=tex,
            callback_data=callback_data,
        )

        builder.button(
            text='↩ К Задачам',
            callback_data=SelectExercises(solution='solution', them=them, task_id=task_id),
        )

        builder.button(
            text='↩ К Заданиям',
            callback_data=SelectExercises(solution='back', them='', task_id=task_id),
        )
        builder.adjust(1, 2)
    return builder.as_markup()
