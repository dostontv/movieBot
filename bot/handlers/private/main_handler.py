from aiogram import Router, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message

from db.models import User

main_router = Router()


@main_router.message(CommandStart())
async def command_start_handler(message: Message, bot: Bot) -> None:
    user_data = message.from_user.model_dump(include={'user_id', 'full_name'})

