import asyncio
import asyncpg
from aiogram import Bot, Dispatcher
import logging
from aiogram.filters import CommandStart
from bots.handlers.callback_plan import select_plan
from bots.handlers.callback_solution import select_solution
from bots.handlers.callback_start import select_start
from bots.handlers.callback_task import select_task
from bots.handlers.callback_tem import select_tem
from bots.handlers.start import get_start
from bots.middlewares.dbmiddleware import DbConnection
from bots.utils.commands import set_commands
from data.config import config_settings
from bots.utils.callbackdata import TaskInfo, SelectTem, SelectSolution, SelectStart


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(config_settings.admin_id, "Бот запущен")

async def stop_bot(bot: Bot):
    await bot.send_message(config_settings.admin_id, "Бот остановлен")

async def create_pool():
    return await asyncpg.create_pool(
        user=config_settings.db_user,
        password=config_settings.db_password.get_secret_value(),
        database=config_settings.db_name,
        host=config_settings.db_host,
        port=config_settings.db_port,
    )

async def start():

    bot = Bot(token=config_settings.bot_token.get_secret_value(), parse_mode="HTML")

    pool_connect = await create_pool()

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    try:
        dp.update.middleware(DbConnection(pool_connect))
        dp.message.register(get_start, CommandStart())
        dp.callback_query.register(select_start, SelectStart.filter())
        dp.callback_query.register(select_task, TaskInfo.filter())
        dp.callback_query.register(select_tem, SelectTem.filter())
        dp.callback_query.register(select_solution, SelectSolution.filter())
        dp.callback_query.register(select_plan)

        await dp.start_polling(bot)

    except Exception as e:
        logging.error(f"An error occurred during bot polling: {e}")
        # Дополнительная информация о состоянии ресурсов или других переменных, которые могут быть полезными при анализе проблемы
        # print(f"Additional information: {some_variable}")
    finally:
        await bot.session.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                               '(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s'
                        )
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(start())
    except KeyboardInterrupt:
        pass
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    finally:
        loop.close()

    # loop = asyncio.get_event_loop()
    # try:
    #     loop.run_until_complete(start())
    # except KeyboardInterrupt:
    #     pass
    # finally:
    #     loop.run_until_complete(loop.shutdown_asyncgens())
    #     loop.close()

# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO,
#                         format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
#                                '(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s'
#                         )
#     asyncio.run(start())
