from aiogram.utils.keyboard import InlineKeyboardBuilder
from bots.utils.back import num
from bots.utils.callbackdata import SelectPlan
from data.get_bd import execute_query


def get_plan(title, task_id):
    builder = InlineKeyboardBuilder()

    query = "SELECT plan_solution FROM plan_title WHERE title = %s"
    params = (title,)
    texts = execute_query(query, params)

    print('', texts)

    for text in texts:
        truncated_text = str(text[0])

        print(truncated_text)

        callback_data = SelectPlan(title=truncated_text, task_id=task_id, back='')
        builder.button(
            text=truncated_text,
            callback_data=callback_data,
        )

        if task_id in num:
            query = ("SELECT t.name_thems FROM exercise e JOIN thems_exercise te ON "
                     "e.title = te.exercise_title JOIN thems t ON "
                     "te.thems_id = t.thems_id WHERE e.title = %s")
            params = (title,)
            task_them = execute_query(query, params)
            them = str(task_them[0]).strip("(),'")

            callback_data = SelectPlan(title='back', task_id=task_id, back=them)
            builder.button(
                text='🔙',
                callback_data=callback_data,
            )
        else:
            callback_data = SelectPlan(title='back', task_id=task_id, back='')
            builder.button(
                text='🔙',
                callback_data=callback_data,
            )

        builder.button(
            text='↩ К Заданиям',
            callback_data=SelectPlan(title='in_task', back='back', task_id=task_id),
        )

        builder.adjust(1, 2)

    return builder.as_markup()
