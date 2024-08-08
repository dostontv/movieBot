import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import BotCommand, BotCommandScopeChat

from bot.handlers import handler_router
from bot.middlewares.channel import ChannelMiddleware
from config import conf
from db.base import Base


async def on_startup(dispatcher: Dispatcher, bot: Bot):
    Base.metadata.create_all(conf.db.db_url)
    dispatcher.include_router(handler_router)
    bot_commands = [
        BotCommand(command="/help", description="Get info about me"),
        BotCommand(command="/send", description="Habar jo'natish")
    ]
    for i in conf.bot.get_admin_list:
        await bot.set_my_commands(bot_commands, BotCommandScopeChat(chat_id=i))


async def on_shutdown(dispatcher: Dispatcher, bot: Bot) -> None:
    await bot.delete_my_commands()
    await dispatcher.storage.close()


async def main() -> None:
    dp = Dispatcher()
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    dp.update.middleware(ChannelMiddleware())
    bot = Bot(token=conf.bot.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
