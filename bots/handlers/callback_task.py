from aiogram.types import CallbackQuery
from bots.keyboards.inline_solution import get_solution
from bots.keyboards.inline_tem import get_tem_task
from bots.utils.callbackdata import TaskInfo
from bots.utils.back import numbers

async def select_task(call: CallbackQuery, callback_data: TaskInfo):
    task_id = callback_data.task_id
    task_tem = callback_data.tem

    if task_tem in numbers:
        tem_kb = get_tem_task(task_id)
        answer = f'Ты выбрал задание {task_id}, выбери тему:'
        await call.message.answer(answer, reply_markup=tem_kb)
    elif task_tem == '20':
        answer = f'Ты выбрал задания которые были в ЕГЭ 2023, выбери задачу:'
        await call.message.answer(answer)
    else:
        answer = f'Ты выбрал задание {task_id}, выбери задачу:'
        await call.message.answer(answer, reply_markup=get_solution(task_id, name_thems=task_tem))
    await call.message.edit_reply_markup(reply_markup=None)
    await call.answer()
