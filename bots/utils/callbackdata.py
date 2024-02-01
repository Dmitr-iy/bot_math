from aiogram.filters.callback_data import CallbackData


class TaskInfo(CallbackData, prefix="task"):
    task_id: int
    tem: str

class SelectTem(CallbackData, prefix="tem"):
    tem_name: str
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
