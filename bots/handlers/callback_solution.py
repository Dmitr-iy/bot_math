from aiogram.types import CallbackQuery
from bots.keyboards.inline_plan import get_plan
from bots.keyboards.inline_task import get_num_task
from bots.utils.back import send_back
from data.get_bd import execute_query


async def select_solution(call: CallbackQuery):
    title = call.data.split(":")[2]

    if title == 'back':
        answer = f'выбери задание:'
        await send_back(call, answer, reply_markup=get_num_task(task_id=title))
    else:
        query = "SELECT condition FROM exercise WHERE title = %s"
        params = (title,)
        texts = execute_query(query, params)

        print(texts)

        if texts:
            answer = f'Задача {texts[0]}'
            await call.message.answer(answer, reply_markup=get_plan(title=title))
            await call.message.edit_reply_markup(reply_markup=None)
        else:
            await call.message.answer("Для этой задачи нет данных.")
