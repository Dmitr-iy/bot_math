from bots.keyboards.inlain_start import get_start_task
from data.dbconnect import Request
from aiogram.types import Message


async def get_start(message: Message, request: Request):
    await request.add_data(message.from_user.id, message.from_user.full_name)
    await message.answer(f"<b>Привет, {message.from_user.full_name}! Выбери номер задания:</b>",
                         reply_markup=get_start_task())

