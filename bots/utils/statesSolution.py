from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State


class PageState(FSMContext):
    page: int = 1

