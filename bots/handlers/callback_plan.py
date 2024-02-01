from aiogram.types import CallbackQuery
from data.get_bd import execute_query


async def select_plan(call: CallbackQuery):
    plan_solution = call.data.split(":")[0]

    query = "SELECT plan_condition FROM solution_plan WHERE plan_solution = %s"
    params = (plan_solution,)
    texts = execute_query(query, params)

    print("Query result:", texts)

    if texts:
        answer = f' {texts[0]}'
        await call.message.answer(answer)
    else:
        await call.message.answer("Для этой задачи нет данных.")
