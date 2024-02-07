from aiogram.types import CallbackQuery
from bots.keyboards.inline_solution import get_solution
from bots.keyboards.inline_task import get_num_task
from bots.utils.back import send_back
from bots.utils.callbackdata import SelectFinish


async def select_finished(call: CallbackQuery, callback_data: SelectFinish):
    back_task = callback_data.back
    task_id = callback_data.task_id

    if back_task == 'back':
        answer = f'выбери задание:'
        await send_back(call, answer, reply_markup=get_num_task(task_id=back_task))
    elif back_task == 'support':
        answer = f'⚙ support 🛠'
        await call.message.answer(answer)
    else:
        answer = f'задание {back_task}, выбери задачу:'
        await send_back(call, answer, reply_markup=get_solution(task_id=task_id, name_thems=back_task))
