from aiogram.utils.keyboard import InlineKeyboardBuilder
from bots.utils.back import number, numbers
from bots.utils.callbackdata import SelectStart, TaskInfo, SelectTem, SelectPlan, SelectExercises, SelectFinish, \
    SelectSolution
from data.get_bd import execute_query


def get_start_task():
    builder = InlineKeyboardBuilder()

    builder.button(
        text='\U0001F4DA Начать \U0001F4C8',
        callback_data=SelectStart(task_id=0)
    )

    return builder.as_markup()


def get_num_task(task_id):
    builder = InlineKeyboardBuilder()

    for task_id in range(1, 21):
        if task_id == 20:
            button_text = "задания которые были в ЕГЭ 2023"
        else:
            button_text = str(task_id)

        builder.button(text=button_text, callback_data=TaskInfo(
            task_id=task_id, tem=str(task_id)))

    builder.adjust(4, 4, 4, 4, 3)
    return builder.as_markup()


def get_tem_task(task_id):
    builder = InlineKeyboardBuilder()

    query = "SELECT thems FROM task_thems WHERE task_id = %s"
    params = (task_id,)
    button_texts = execute_query(query, params)

    print("", button_texts)

    for button_text in button_texts:

        builder.button(
            text=button_text[0],
            callback_data=SelectTem(task_id=task_id, tem_name=str(button_text[0]), back=str()),
        )

    builder.button(
        text='🔙',
        callback_data=SelectTem(task_id=task_id, tem_name=str(), back='back'),
    )

    builder.adjust(1, 1, 1, 1, 1)

    # if task_id in [1, 6, 7, 16]:
    #     builder.adjust(2, 1)
    # elif task_id == 3:
    #     builder.adjust(1, 2, 2)
    # elif task_id == 10:
    #     builder.adjust(2, 2, 1, 1)
    # elif task_id in [11, 13, 15, 18]:
    #     builder.adjust(1, 1)

    return builder.as_markup()


def get_solution(task_id, name_thems):
    print("Task ID:", task_id)
    print("Name thems:", name_thems)

    builder = InlineKeyboardBuilder()

    query = ""
    params = ()
    num = number

    if task_id in num:
        query = "SELECT exercise_title FROM task_exercise WHERE task_id = %s"
        params = (task_id,)
    else:
        query = "SELECT e.title FROM exercise e JOIN thems_exercise te ON" \
                " e.title = te.exercise_title JOIN thems t ON te.thems_id = t.thems_id" \
                " WHERE t.name_thems = %s"
        params = (name_thems,)

    button_texts = execute_query(query, params)

    print("Query:", query)
    print("Params:", params)

    print("Button texts:", button_texts)

    for button_text in button_texts:
        callback_data = SelectSolution(task_id=task_id, title=button_text[0])
        builder.button(
            text=button_text[0],
            callback_data=callback_data,
        )

    builder.button(
        text='🔙',
        callback_data=SelectSolution(task_id=task_id, title='back'),
    )

    if task_id == 9:
        builder.adjust(1, 2, 2)
    elif task_id == 19:
        builder.adjust(1, 1, 1, 1, 1)
    else:
        builder.adjust(1, 1, 1, 1, 1)

    return builder.as_markup()


def get_plan(title, task_id):
    builder = InlineKeyboardBuilder()

    query = "SELECT plan_solution FROM plan_title WHERE title = %s"
    params = (title,)
    texts = execute_query(query, params)

    query = ("SELECT t.name_thems FROM exercise e JOIN thems_exercise te ON "
             "e.title = te.exercise_title JOIN thems t ON "
             "te.thems_id = t.thems_id WHERE e.title = %s")
    params = (title,)
    task_them = execute_query(query, params)

    print('2TEXTS', texts)
    if task_id in numbers:
        them = str(task_them[0]).strip("(),'")
    else:
        them = str(task_them)

    for text in texts:
        truncated_text = str(text[0])

        print(truncated_text)

        callback_data = SelectPlan(title=truncated_text, task_id=task_id, back=them)
        builder.button(
            text=truncated_text,
            callback_data=callback_data,
        )

        callback_data = SelectPlan(title='back', back=them, task_id=task_id)
        builder.button(
            text='🔙',
            callback_data=callback_data,
        )

        builder.button(
            text='↩ К Заданиям',
            callback_data=SelectPlan(title='in_task', back='back', task_id=task_id),
        )

        builder.adjust(1, 2)

    return builder.as_markup()


def get_exercises(solution, task_id, them):
    print("Solution:", solution)
    print("Task EXER:", task_id)
    print("Them EXER:", them)
    builder = InlineKeyboardBuilder()

    query = "SELECT sol_plan_title FROM plan_title WHERE plan_solution = %s"
    params = (solution,)
    texts = execute_query(query, params)
    print(texts)

    for text in texts:
        tex = str(text[0])
        print(tex)
        callback_data = SelectExercises(solution=tex, them=them, task_id=task_id)
        builder.button(
            text=tex,
            callback_data=callback_data,
        )

        builder.button(
            text='↩ К Задачам',
            callback_data=SelectExercises(solution='solution', them=them, task_id=task_id),
        )

        builder.button(
            text='↩ К Заданиям',
            callback_data=SelectExercises(solution='back', them='', task_id=task_id),
        )
        builder.adjust(1, 2)
    return builder.as_markup()


def get_finish(task_id, name_them):
    print("Task Finished:", task_id)
    print("Finish thems:", name_them)

    builder = InlineKeyboardBuilder()

    builder.button(
        text="VK",
        url="https://vk.com/koshelevgeniya"
    )
    builder.button(
        text="контакт Telegram",
        url="https://t.me/evgeniyaKoshel"
    )

    builder.button(
        text='↩ К Задачам',
        callback_data=SelectFinish(back=name_them, task_id=task_id),
    )

    builder.button(
        text='↩ К Заданиям',
        callback_data=SelectFinish(back='back', task_id=task_id),
    )

    builder.button(
        text='⚙ support 🛠',
        callback_data=SelectFinish(back='support', task_id=task_id),
    )

    builder.adjust(2, 2)

    return builder.as_markup()
