# import logging
# import psycopg2
# from aiogram.utils.keyboard import InlineKeyboardBuilder
# from bots.utils.callbackdata import SelectTem
#
#
# def get_tem_task(task_id):
#     builder = InlineKeyboardBuilder()
#
#     try:
#         conn = psycopg2.connect(dbname='bot_math', user='postgres', password='password', host='localhost')
#         cursor = conn.cursor()
#
#         cursor.execute("SELECT thems FROM task_thems WHERE task_id = %s", (task_id,))
#         button_texts = cursor.fetchall()
#
#         print("", button_texts)
#
#         # Создаем кнопки на основе данных из базы данных
#         for button_text in button_texts:
#             builder.button(
#                 text=button_text[0],  # Предполагается, что возвращается единственное значение текста кнопки
#                 callback_data=SelectTem(task_id=task_id, tem_name=str(button_text[0])),
#             )
#     except Exception as e:
#         logging.error(f"Произошла ошибка при работе с базой данных: {e}", exc_info=True)
#         # Обработка ошибки, например, возврат пустой клавиатуры или других действий
#     finally:
#         if cursor:
#             cursor.close()
#         if conn:
#             conn.close()
#
#     if task_id in [1, 6, 7, 16]:
#         builder.adjust(2, 1)
#     elif task_id == 3:
#         builder.adjust(1, 2, 2)
#     elif task_id == 10:
#         builder.adjust(2, 2, 1, 1)
#     elif task_id in [11, 13, 15, 18]:
#         builder.adjust(1, 1)
#
#     return builder.as_markup()


from aiogram.utils.keyboard import InlineKeyboardBuilder
from bots.utils.callbackdata import SelectTem
from data.get_bd import execute_query


def get_tem_task(task_id):
    builder = InlineKeyboardBuilder()

    query = "SELECT thems FROM task_thems WHERE task_id = %s"
    params = (task_id,)
    button_texts = execute_query(query, params)

    print("", button_texts)

    # Создаем кнопки на основе данных из базы данных
    for button_text in button_texts:

        builder.button(
            text=button_text[0],
            callback_data=SelectTem(task_id=task_id, tem_name=str(button_text[0]), back=str()),
        )

    builder.button(
        text='Назад',
        callback_data=SelectTem(task_id=task_id, tem_name=str(), back='back'),
    )

    # Остальной код функции остается без изменений
    if task_id in [1, 6, 7, 16]:
        builder.adjust(2, 1)
    elif task_id == 3:
        builder.adjust(1, 2, 2)
    elif task_id == 10:
        builder.adjust(2, 2, 1, 1)
    elif task_id in [11, 13, 15, 18]:
        builder.adjust(1, 1)

    return builder.as_markup()
