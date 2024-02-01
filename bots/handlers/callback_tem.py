from aiogram.types import CallbackQuery
from bots.keyboards.inline_solution import get_solution
from bots.utils.callbackdata import SelectTem


async def select_tem(call: CallbackQuery, callback_data: SelectTem):
    tem_kb = callback_data.tem_name
    task_id = callback_data.task_id
    answer = f'Ты выбрал тему {tem_kb}, выбери задачу:'
    await call.message.answer(answer, reply_markup=get_solution(task_id, name_thems=tem_kb))
    await call.answer()
