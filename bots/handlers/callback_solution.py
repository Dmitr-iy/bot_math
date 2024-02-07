from aiogram.types import CallbackQuery
from bots.keyboards.inline_plan import get_plan
from bots.keyboards.inline_task import get_num_task
from bots.keyboards.inline_tem import get_tem_task
from bots.utils.back import send_back
from bots.utils.back import numbers
from data.get_bd import execute_query


async def select_solution(call: CallbackQuery):
    title = call.data.split(":")[2]
    task_id = call.data.split(":")[1]

    print(title)
    print(task_id)

    if title == 'back':
        if task_id in numbers:
            answer = f'Ты выбрал задание {task_id}, выбери тему:'
            await send_back(call, answer, reply_markup=get_tem_task(task_id=str(task_id)))
        else:
            answer = f'выбери задание:'
            await send_back(call, answer, reply_markup=get_num_task(task_id=str(task_id)))
    else:
        query = "SELECT condition FROM exercise WHERE title = %s"
        params = (title,)
        texts = execute_query(query, params)

        print(texts)

        if texts:
            answer = f'Задача {texts[0]}'
            await call.message.answer(answer, reply_markup=get_plan(title=title, task_id=task_id))
            await call.message.edit_reply_markup(reply_markup=None)
        else:
            await call.message.answer("Для этой задачи нет данных.")
