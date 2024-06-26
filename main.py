import asyncio
import asyncpg
from aiogram import Bot, Dispatcher
import logging
from bots.handlers.handler import router
from bots.middlewares.dbmiddleware import DbConnection
from bots.utils.commands import set_commands
from data.config import config_settings
from bots.utils.callbackdata import TaskInfo, SelectTem, SelectSolution, SelectStart, SelectPlan, SelectExercises, \
    SelectFinish


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
    dp.update.middleware(DbConnection(pool_connect))
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    try:
        dp.include_router(router)

        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)

    except Exception as e:
        logging.error(f"An error occurred during bot polling: {e}")
        await bot.send_message(config_settings.admin_id, f"An error occurred during bot polling: {e}")
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
