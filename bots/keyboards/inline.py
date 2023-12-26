from aiogram.utils.keyboard import InlineKeyboardBuilder
from bots.utils.callbackdata import TaskInfo, SelectTem


def get_num_task():
    builder = InlineKeyboardBuilder()

    for task_id in range(1, 21):
        if task_id == 20:
            button_text = "задания которые были в ЕГЭ 2023"
        else:
            button_text = str(task_id)
        builder.button(text=button_text, callback_data=TaskInfo(task_id=task_id, tem=str(task_id), solution='Задания'))

    builder.adjust(4, 4, 4, 4, 3)
    return builder.as_markup()


def get_tem_task(task_id):
    builder = InlineKeyboardBuilder()

    if task_id == 1:
        builder.button(text="Треугольник", callback_data=SelectTem(tem_name="Треугольник", solution="Задания"))
        builder.button(text="Окружность", callback_data=SelectTem(tem_name="Окружность", solution="Задания"))
        builder.button(text="Прямоугольный треугольник", callback_data=SelectTem(tem_name="Прямоуг. треугольник",
                                                                                 solution="Задания"))
        builder.adjust(2)
    elif task_id == 3:
        builder.button(text="комбинация треуг", callback_data=SelectTem(tem_name="комбинация треуг",
                                                                        solution="Задания"))
        builder.button(text="пирамида", callback_data=SelectTem(tem_name="пирамида", solution="Задания"))
        builder.button(text="конус", callback_data=SelectTem(tem_name="конус", solution="Задания"))
        builder.button(text="цилиндр", callback_data=SelectTem(tem_name="цилиндр", solution="Задания"))
        builder.button(text="призма", callback_data=SelectTem(tem_name="призма", solution="Задания"))
        builder.button(text="куб/параллелепипед", callback_data=SelectTem(tem_name="куб/параллелепипед",
                                                                          solution="Задания"))
        builder.adjust(1, 2, 2)
    elif task_id == 6:
        builder.button(text="тригонометрия", callback_data=SelectTem(tem_name="тригонометрия", solution="Задания"))
        builder.button(text="не тригонометрия", callback_data=SelectTem(tem_name="не тригонометрия",
                                                                        solution="Задания"))
        builder.adjust(1)
    elif task_id == 7:
        builder.button(text="логорифмы", callback_data=SelectTem(tem_name="логорифмы", solution="Задания"))
        builder.button(text="подстановка", callback_data=SelectTem(tem_name="подстановка", solution="Задания"))
        builder.button(text="тригонометрия", callback_data=SelectTem(tem_name="тригонометрия", solution="Задания"))
        builder.adjust(1, 1)
    elif task_id == 8:
        builder.button(text="с графиком производной", callback_data=SelectTem(tem_name="с графиком производной",
                                                                              solution="Задания"))
        # builder.button(text="подстановка", callback_data=SelectTem(tem_name="2"))
    elif task_id == 10:
        builder.button(text="сплавы и смеси", callback_data=SelectTem(tem_name="сплавы и смеси", solution="Задания"))
        builder.button(text="движение по воде", callback_data=SelectTem(tem_name="движение по воде",
                                                                        solution="Задания"))
        builder.button(text="совместная работа", callback_data=SelectTem(tem_name="совместная работа",
                                                                         solution="Задания"))
        builder.button(text="производительность", callback_data=SelectTem(tem_name="производительность",
                                                                          solution="Задания"))
        builder.button(text="движение по прямой", callback_data=SelectTem(tem_name="движение по прямой",
                                                                          solution="Задания"))
        builder.button(text="движение по окружности", callback_data=SelectTem(tem_name="движение по окружности",
                                                                              solution="Задания"))
        builder.adjust(1, 1, 1, 1, 1)
    elif task_id == 11:
        builder.button(text="найти значение функции", callback_data=SelectTem(tem_name="значение функции",
                                                                              solution="Задания"))
        builder.button(text="найти абсциссу точки пересечения", callback_data=SelectTem(
            tem_name="абсцисса", solution="Задания"))
        # builder.button(text="совместная работа", callback_data=SelectTem(tem_name="3", solution="Задания"))
        # builder.button(text="производительность", callback_data=SelectTem(tem_name="4", solution="Задания"))
        # builder.button(text="движение по прямой", callback_data=SelectTem(tem_name="5", solution=""))
        # builder.button(text="движение по окружности", callback_data=SelectTem(tem_name="6", solution="Задания"))
        builder.adjust(1)
    elif task_id == 13:
        builder.button(text="тригонометрия", callback_data=SelectTem(tem_name="тригонометрия", solution="Задания"))
        builder.button(text="не тригонометрия", callback_data=SelectTem(tem_name="не тригонометрия",
                                                                        solution="Задания"))
        builder.adjust(1)
    elif task_id == 15:
        builder.button(text="логарифмические неравенства", callback_data=SelectTem(
            tem_name="логарифм", solution="Задания"))
        builder.button(text="показательные неравенства", callback_data=SelectTem(tem_name="показательные",
                                                                                 solution="Задания"))
        builder.adjust(1)
    elif task_id == 16:
        builder.button(text="вклады", callback_data=SelectTem(tem_name="вклады", solution="Задания"))
        builder.button(text="оптимизация", callback_data=SelectTem(tem_name="оптимизация", solution="Задания"))
        builder.button(text="кредиты равные платежи", callback_data=SelectTem(tem_name="кредиты равные платежи",
                                                                              solution="Задания"))
        builder.button(text="кредиты разные платежи", callback_data=SelectTem(tem_name="кредиты разные платежи",
                                                                              solution="Задания"))
        builder.adjust(2, 1)
    elif task_id == 18:
        builder.button(text="будет что то", callback_data=SelectTem(tem_name="будет что т", solution="Задания"))
        builder.button(text="когда то", callback_data=SelectTem(tem_name="когда то", solution="Задания"))
        builder.button(text="наверное", callback_data=SelectTem(tem_name="наверное", solution="Задания"))
        builder.adjust(2)

    return builder.as_markup()
