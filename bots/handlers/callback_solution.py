from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from bots.keyboards.inline_plan import get_plan
from bots.keyboards.inline_task import get_num_task
from bots.utils.statesSolution import Form
from data.get_bd import execute_query


async def select_solution(call: CallbackQuery, state: FSMContext):
    title = call.data.split(":")[2]

    if title == 'back':
        answer = f'выбери задание:'
        await call.message.answer(answer, reply_markup=get_num_task(task_id=title))
        await call.message.edit_reply_markup(reply_markup=None)
        await call.answer()
        await state.set_state(Form.task_num)
    else:

        query = "SELECT condition FROM exercise WHERE title = %s"
        params = (title,)
        texts = execute_query(query, params)

        print(texts)

        if texts:
            answer = f'Задача {texts[0]}'
            await call.message.answer(answer, reply_markup=get_plan(title=title))
            await state.update_data(task=call.data)
            await call.message.edit_reply_markup(reply_markup=None)
            await state.set_state(Form.plan)
        else:
            await call.message.answer("Для этой задачи нет данных.")
