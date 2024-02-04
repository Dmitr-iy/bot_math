from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from bots.keyboards.inline_solution import get_solution
from bots.keyboards.inline_task import get_num_task
from bots.utils.callbackdata import SelectTem
from bots.utils.statesSolution import Form


async def select_tem(call: CallbackQuery, callback_data: SelectTem, state: FSMContext):
    tem_kb = callback_data.tem_name
    task_id = callback_data.task_id
    back = callback_data.back

    if back:
        answer = f' выбери задание:'
        await call.message.answer(answer, reply_markup=get_num_task(task_id))
        await call.message.edit_reply_markup(reply_markup=None)
        await call.answer()
        await state.set_state(Form.task_num)
    else:

        answer = f'Ты выбрал тему {tem_kb}, выбери задачу:'
        await call.message.answer(answer, reply_markup=get_solution(task_id, name_thems=tem_kb))
        await state.update_data(tem=call.data)
        await call.message.edit_reply_markup(reply_markup=None)
        await call.answer()
        await state.set_state(Form.task)
