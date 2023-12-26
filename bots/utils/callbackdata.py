from aiogram.filters.callback_data import CallbackData


class TaskInfo(CallbackData, prefix="task"):
    task_id: int
    tem: str
    solution: str

class SelectTem(CallbackData, prefix="tem"):
    tem_name: str
    solution: str
