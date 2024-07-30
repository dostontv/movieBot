import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode, BotCommandScopeType
from aiogram.types import BotCommand, BotCommandScopeChat, BotCommandScopeDefault

from bot.handlers import handler_router
from bot.middlewares.channel import CounterMiddleware
from config import conf
from db.base import Base


async def on_startup(dispatcher: Dispatcher, bot: Bot):
    bot_commands = [
        BotCommand(command="/help", description="Get info about me"),
        BotCommand(command="/qna", description="set bot for a QnA task"),
        BotCommand(command="/chat", description="set bot for free chat")
    ]
    await bot.set_my_commands(bot_commands, BotCommandScopeChat(type=BotCommandScopeType.ALL_PRIVATE_CHATS,chat_id=6498606371))


async def main() -> None:
    dp = Dispatcher()
    dp.include_router(handler_router)
    dp.update.middleware(CounterMiddleware())
    dp.startup.register(on_startup)
    Base.metadata.create_all(conf.db.db_url)
    bot = Bot(token=conf.bot.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
