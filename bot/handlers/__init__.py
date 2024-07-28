from aiogram import Router

from bot.handlers.private import private_handler_router
from bot.handlers.inline_show import inline_show_router
handler_router = Router()

handler_router.include_routers(
    private_handler_router ,
    inline_show_router
)