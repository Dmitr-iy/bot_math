from aiogram.types import CallbackQuery
from bots.keyboards.inlain_exer import get_exercises
from bots.keyboards.inline_task import get_num_task
from bots.utils.back import send_back
from bots.utils.callbackdata import SelectPlan
from data.get_bd import execute_query


async def select_plan(call: CallbackQuery, callback_data: SelectPlan):
    plan_solution = callback_data.title

    print("Select:", plan_solution)

    if plan_solution == 'back':
        answer = f'выбери задание:'
        await send_back(call, answer, reply_markup=get_num_task(task_id=plan_solution))
    else:
        query = "SELECT plan_condition FROM solution_plan WHERE plan_solution = %s"
        params = (plan_solution,)
        texts = execute_query(query, params)

        print("Query rlt:", texts)

        if texts:
            answer = f' {texts[0]}'
            await call.message.answer(answer, reply_markup=get_exercises(solution=plan_solution))
            await call.message.edit_reply_markup(reply_markup=None)
        else:
            await call.message.answer("Ошибка базы данных, повторите попытку.")
