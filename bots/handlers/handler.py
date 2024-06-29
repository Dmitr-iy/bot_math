from aiogram import Router
from aiogram.filters import CommandStart
from bots.keyboards.inlain import (get_start_task, get_finish, get_exercises, get_plan, get_solution,
                                   get_num_task, get_tem_task)
from bots.utils.back import send_back, numbers
from bots.utils.callbackdata import SelectTem, SelectStart, TaskInfo, SelectPlan, SelectFinish, SelectExercises, \
    SelectSolution
from data.dbconnect import Request
from aiogram.types import Message, CallbackQuery
from data.get_bd import execute_query


router = Router()

@router.message(CommandStart())
async def get_start(message: Message, request: Request):
    await request.add_data(message.from_user.id, message.from_user.full_name)
    await message.answer(f"<b>Привет, {message.from_user.full_name}! Выбери номер задания:⬇ ⬇ ⬇ ⬇ ⬇</b>",
                         reply_markup=get_start_task())


@router.callback_query(SelectStart.filter())
async def select_start(call: CallbackQuery, callback_data: SelectStart):
    task_id = callback_data.task_id
    answer = f'Выбери задание:'
    await call.message.answer(answer, reply_markup=get_num_task(task_id))
    await call.message.edit_reply_markup(reply_markup=None)
    await call.answer()


@router.callback_query(TaskInfo.filter())
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


@router.callback_query(SelectTem.filter())
async def select_tem(call: CallbackQuery, callback_data: SelectTem):
    tem_kb = callback_data.tem_name
    task_id = callback_data.task_id
    back = callback_data.back

    if back:
        answer = f' выбери задание:'
        await send_back(call, answer, reply_markup=get_num_task(task_id))
    else:
        answer = f'Ты выбрал тему {tem_kb}, выбери задачу:'
        await call.message.answer(answer, reply_markup=get_solution(task_id, name_thems=tem_kb))
        await call.message.edit_reply_markup(reply_markup=None)
        await call.answer()


@router.callback_query(SelectSolution.filter())
async def select_solution(call: CallbackQuery, callback_data: SelectSolution):
    title = callback_data.title
    task_id = callback_data.task_id
    # title = call.data.split(":")[2]
    # task_id = call.data.split(":")[1]

    print('Title', title)
    print('task_id', task_id)

    if title == 'back':
        if task_id in numbers:
            answer = f'Ты выбрал задание {task_id}, выбери тему:'
            await send_back(call, answer, reply_markup=get_tem_task(task_id=str(task_id)))
        else:
            answer = f'выбери задание:'
            await send_back(call, answer, reply_markup=get_num_task(task_id=str(task_id)))
    else:
        # query = "SELECT condition FROM exercise WHERE title = %s"
        query = "SELECT `condition` FROM exercise WHERE title = %s"
        print('QUERY', query)
        params = (title,)
        texts = execute_query(query, params)

        print('TEXTS', texts)

        if texts:
            answer = f'Задача {texts[0]}'
            await call.message.answer(answer, reply_markup=get_plan(title=title, task_id=task_id))
            await call.message.edit_reply_markup(reply_markup=None)
        else:
            await call.message.answer("Для этой задачи нет данных.")

@router.callback_query(SelectPlan.filter())
async def select_plan(call: CallbackQuery, callback_data: SelectPlan):
    plan_solution = callback_data.title
    task_id = callback_data.task_id
    back = callback_data.back

    print('Back', back)
    print("Select:", plan_solution)
    print("Task ID:", task_id)

    if plan_solution == 'back':
        answer = f'задание {task_id}, выбери задачу:'
        await send_back(call, answer, reply_markup=get_solution(task_id=task_id, name_thems=back))
    elif plan_solution == 'in_task':
        answer = f'Выбери задание:'
        await send_back(call, answer, reply_markup=get_num_task(task_id=task_id))
    else:
        query = "SELECT plan_condition FROM solution_plan WHERE plan_solution = %s"
        params = (plan_solution,)
        texts = execute_query(query, params)

        print("Query rlt:", texts)

        if texts:
            answer = f' {texts[0]}'
            await call.message.answer(answer, reply_markup=get_exercises(solution=plan_solution, task_id=task_id,
                                                                         them=back))
            await call.message.edit_reply_markup(reply_markup=None)
        else:
            await call.message.answer("Ошибка базы данных, повторите попытку.")

@router.callback_query(SelectExercises.filter())
async def select_exercises(call: CallbackQuery, callback_data: SelectExercises):
    sol = callback_data.solution
    task_id = callback_data.task_id
    name_them = callback_data.them
    print("TEMA: ", name_them)
    print("select", sol)

    if sol == 'back':
        answer = f'выбери задание:'
        await send_back(call, answer, reply_markup=get_num_task(task_id=sol))
    elif sol == 'solution':
        answer = f'задание {task_id}, выбери задачу:'
        await send_back(call, answer, reply_markup=get_solution(task_id=task_id, name_thems=name_them))
    else:
        query = "SELECT solutions FROM solution WHERE sol = %s"
        params = (sol,)
        tex = execute_query(query, params)
        print("Solution", tex)
        if tex:
            answer = f'Решение: {tex[0][0]}'
            await call.message.answer(answer, reply_markup=get_finish(task_id=task_id, name_them=name_them))
            await call.message.edit_reply_markup(reply_markup=None)
        else:
            await call.message.answer("Для этой задачи нет данных.")

@router.callback_query(SelectExercises.filter())
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
