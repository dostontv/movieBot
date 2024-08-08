import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import BotCommand, BotCommandScopeChat
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

from bot.handlers import handler_router
from bot.middlewares.channel import ChannelMiddleware
from config import conf
from db.base import Base


async def on_startup(dispatcher: Dispatcher, bot: Bot):
    await bot.set_webhook(f"{conf.bot.BASE_WEBHOOK_URL}{conf.bot.WEBHOOK_PATH}", secret_token=conf.bot.WEBHOOK_SECRET,
                          drop_pending_updates=True)

    Base.metadata.create_all(conf.db.db_url)
    dispatcher.include_router(handler_router)
    bot_commands = [
        BotCommand(command="/help", description="Get info about me"),
        BotCommand(command="/send", description="Habar jo'natish")
    ]
    for i in conf.bot.get_admin_list:
        await bot.set_my_commands(bot_commands, BotCommandScopeChat(chat_id=i))


async def on_shutdown(dispatcher: Dispatcher, bot: Bot) -> None:
    await bot.delete_webhook()
    await bot.delete_my_commands()
    await dispatcher.storage.close()


def main() -> None:
    dp = Dispatcher()
    dp.startup.register(on_startup)
    dp.update.middleware(ChannelMiddleware())

    bot = Bot(token=conf.bot.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    app = web.Application()
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
        secret_token=conf.bot.WEBHOOK_SECRET,
    )
    webhook_requests_handler.register(app, path=conf.bot.WEBHOOK_PATH)

    setup_application(app, dp, bot=bot)

    web.run_app(app, host=conf.bot.WEB_SERVER_HOST, port=conf.bot.WEB_SERVER_PORT)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    main()
