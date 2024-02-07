from aiogram.types import CallbackQuery
from bots.keyboards.inlaine_finish import get_finish
from bots.keyboards.inline_solution import get_solution
from bots.keyboards.inline_task import get_num_task
from bots.utils.back import send_back
from bots.utils.callbackdata import SelectExercises
from data.get_bd import execute_query


async def select_exercises(call: CallbackQuery, callback_data: SelectExercises):
    sol = callback_data.solution
    task_id = callback_data.task_id
    name_them = callback_data.them
    print("TEMA: ", name_them)
    print("select", sol)

    if sol == 'back':
        answer = f'выбери задание:'
        await send_back(call, answer, reply_markup=get_num_task(task_id=sol))
    elif sol == 'solution':
        answer = f'задание {task_id}, выбери задачу:'
        await send_back(call, answer, reply_markup=get_solution(task_id=task_id, name_thems=name_them))
    else:
        query = "SELECT solutions FROM solution WHERE sol = %s"
        params = (sol,)
        tex = execute_query(query, params)
        print("Solution", tex)
        if tex:
            answer = f'Решение: {tex[0][0]}'
            await call.message.answer(answer, reply_markup=get_finish())
            await call.message.edit_reply_markup(reply_markup=None)
        else:
            await call.message.answer("Для этой задачи нет данных.")
