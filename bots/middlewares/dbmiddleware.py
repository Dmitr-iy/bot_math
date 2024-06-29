from typing import Any, Callable, Dict, Awaitable
import aiomysql
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from data.dbconnect import Request


class DbConnection(BaseMiddleware):
    def __init__(self, connector: aiomysql.pool):
        super().__init__()
        self.connector = connector

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        async with self.connector.acquire() as connect:
            data["request"] = Request(connect)
            return await handler(event, data)
