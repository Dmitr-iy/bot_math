from aiogram.filters.callback_data import CallbackData


class SelectStart(CallbackData, prefix="start"):
    task_id: int

class TaskInfo(CallbackData, prefix="task"):
    task_id: int
    tem: str

class SelectTem(CallbackData, prefix="tem"):
    tem_name: str
    back: str
    task_id: int

class SelectSolution(CallbackData, prefix="solution"):
    task_id: int
    title: str

class SelectPlan(CallbackData, prefix="plan"):
    title: str
    back: str
    task_id: int


class SelectExercises(CallbackData, prefix="sol"):
    solution: str
    back: str

class SelectFinish(CallbackData, prefix="finish"):
    back: str
    support: str
