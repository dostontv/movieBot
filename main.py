import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv

from bot.handlers import handler_router
from config import conf
from db.base import Base

load_dotenv('.env')

async def main() -> None:
    dp = Dispatcher()
    dp.include_router(handler_router)
    Base.metadata.create_all(conf.db.db_url)

    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=conf.bot.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
