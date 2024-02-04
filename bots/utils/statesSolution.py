from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    task_num = State()
    tem = State()
    task = State()
    solution = State()
    plan = State()
