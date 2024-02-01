from aiogram.types import CallbackQuery
from bots.keyboards.inline_plan import get_plan
from data.get_bd import execute_query


async def select_solution(call: CallbackQuery):
    title = call.data.split(":")[2]

    query = "SELECT condition FROM exercise WHERE title = %s"
    params = (title,)
    texts = execute_query(query, params)

    print(texts)

    if texts:
        answer = f'Задача {texts[0]}'
        await call.message.answer(answer, reply_markup=get_plan(title=title))
    else:
        await call.message.answer("Для этой задачи нет данных.")
