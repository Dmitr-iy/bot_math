from aiogram.types import CallbackQuery
from bots.keyboards.inline_task import get_num_task
from bots.utils.back import send_back
from bots.utils.callbackdata import SelectFinish


async def select_finished(call: CallbackQuery, callback_data: SelectFinish):
    back_task = callback_data.back

    if back_task == 'back':
        answer = f'выбери задание:'
        await send_back(call, answer, reply_markup=get_num_task(task_id=back_task))
    else:
        answer = f'К поддержке'
        await call.message.answer(answer)
