from aiogram.filters.callback_data import CallbackData


class SelectStart(CallbackData, prefix="start"):
    task_id: int

class TaskInfo(CallbackData, prefix="task"):
    task_id: int
    tem: str

class SelectTem(CallbackData, prefix="tem"):
    tem_name: str
    back: str
    # solution: str
    task_id: int
    # tem: str

class SelectSolution(CallbackData, prefix="solution"):
    task_id: int
    title: str
    # page: int

class SelectPlan(CallbackData, prefix="plan"):
    title: str
    condition: str
    # task_id: int
