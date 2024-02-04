# from aiogram.fsm.context import FSMContext
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from bots.keyboards.inline_task import get_num_task
from bots.utils.callbackdata import SelectStart
from bots.utils.statesSolution import Form


async def select_start(call: CallbackQuery, callback_data: SelectStart, state: FSMContext):
    task_id = callback_data.task_id
    answer = f'Выбери задание:'
    await call.message.answer(answer, reply_markup=get_num_task(task_id))
    await call.message.edit_reply_markup(reply_markup=None)
    await call.answer()
    await state.set_state(Form.task_num)
