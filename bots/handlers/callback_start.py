from aiogram.types import CallbackQuery
from bots.keyboards.inline_task import get_num_task
from bots.utils.callbackdata import SelectStart


async def select_start(call: CallbackQuery, callback_data: SelectStart):
    task_id = callback_data.task_id
    answer = f'Выбери задание:'
    await call.message.answer(answer, reply_markup=get_num_task(task_id))
    await call.message.edit_reply_markup(reply_markup=None)
    await call.answer()
