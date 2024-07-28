import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from bot.handlers import private_handler_router
from config import Configuration


async def main() -> None:
    dp = Dispatcher()
    dp.include_router(private_handler_router)

    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=Configuration.bot.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
