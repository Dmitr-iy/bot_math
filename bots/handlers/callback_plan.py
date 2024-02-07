from aiogram.types import CallbackQuery
from bots.keyboards.inlain_exer import get_exercises
from bots.keyboards.inline_solution import get_solution
from bots.keyboards.inline_task import get_num_task
from bots.utils.back import send_back
from bots.utils.callbackdata import SelectPlan
from data.get_bd import execute_query


async def select_plan(call: CallbackQuery, callback_data: SelectPlan):
    plan_solution = callback_data.title
    task_id = callback_data.task_id
    back = callback_data.back

    print('Back', back)
    print("Select:", plan_solution)
    print("Task ID:", task_id)

    if plan_solution == 'back':
        answer = f'задание {task_id}, выбери задачу:'
        await send_back(call, answer, reply_markup=get_solution(task_id=task_id, name_thems=back))
    elif plan_solution == 'in_task':
        answer = f'Выбери задание:'
        await send_back(call, answer, reply_markup=get_num_task(task_id=task_id))
    else:
        query = "SELECT plan_condition FROM solution_plan WHERE plan_solution = %s"
        params = (plan_solution,)
        texts = execute_query(query, params)

        print("Query rlt:", texts)

        if texts:
            answer = f' {texts[0]}'
            await call.message.answer(answer, reply_markup=get_exercises(solution=plan_solution, task_id=task_id,
                                                                         them=back))
            await call.message.edit_reply_markup(reply_markup=None)
        else:
            await call.message.answer("Ошибка базы данных, повторите попытку.")
