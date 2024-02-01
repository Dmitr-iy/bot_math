from bots.keyboards.inline_task import get_num_task
from data.dbconnect import Request
from aiogram import Bot
from aiogram.types import Message


async def get_start(message: Message, bot: Bot, request: Request):
    await request.add_data(message.from_user.id, message.from_user.full_name)
    await message.answer(f"<b>Привет, {message.from_user.full_name}! Выбери номер задания:</b>",
                         reply_markup=get_num_task())

