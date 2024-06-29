from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command="start", description="Старт"
        ),
        BotCommand(
            command="help", description="Помощь"
        ),
        BotCommand(
            command="info", description="Информация"
        ),
        BotCommand(
            command='message', description='Сообщение'
        ),
        BotCommand(
            command='task', description='Задание'
        ),
        BotCommand(
            command='all tem', description='Все темы'
        ),
    ]
    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())
