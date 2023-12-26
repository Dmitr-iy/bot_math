from aiogram import Bot
from aiogram.types import CallbackQuery
from bots.keyboards.inline import get_tem_task
from bots.utils.callbackdata import TaskInfo, SelectTem


async def select_task(call: CallbackQuery, bot: Bot, callback_data: TaskInfo):
    task_info = callback_data.task_id
    task_tem = callback_data.tem
    sol = callback_data.solution

    if task_tem in ['1', '3', '6', '7', '8', '10', '11', '13', '15', '16', '18']:
        tem_kb = get_tem_task(task_info)
        answer = f'Ты выбрал задание {task_info}, выбери тему:'
        await call.message.answer(answer, reply_markup=tem_kb)
    elif task_tem == '20':
        answer = f'Ты выбрал задания которые были в ЕГЭ 2023, вот решения: {sol}'
        await call.message.answer(answer)
    else:
        answer = f'Ты выбрал задание {task_info}, вот решения: {sol}'
        await call.message.answer(answer)
    await call.answer()


async def select_tem(call: CallbackQuery, bot: Bot, callback_data: SelectTem):
    tem_kb = callback_data.tem_name
    solution = callback_data.solution
    answer = f'Ты выбрал тему {tem_kb}, вот решения: {solution}'
    await call.message.answer(answer)
