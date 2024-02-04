from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from bots.keyboards.inline_task import get_num_task
from bots.utils.statesSolution import Form
from data.get_bd import execute_query


async def select_plan(call: CallbackQuery, state: FSMContext):
    plan_solution = call.data.split(":")[0]

    if plan_solution == 'back':
        answer = f'выбери задание:'
        await call.message.answer(answer, reply_markup=get_num_task(task_id=plan_solution))
        await call.message.edit_reply_markup(reply_markup=None)
        await call.answer()
        await state.set_state(Form.task_num)

    else:

        query = "SELECT plan_condition FROM solution_plan WHERE plan_solution = %s"
        params = (plan_solution,)
        texts = execute_query(query, params)

        print("Query result:", texts)

        if texts:
            answer = f' {texts[0]}'
            await call.message.answer(answer)
            await state.update_data(plan=call.data)
            await call.message.edit_reply_markup(reply_markup=None)
            await state.set_state(Form.solution)
        else:
            await call.message.answer("Для этой задачи нет данных.")
