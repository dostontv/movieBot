from aiogram import Router, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message

from db.models import User

main_router = Router()


@main_router.message(CommandStart())
async def command_start_handler(message: Message, bot: Bot) -> None:
    user_data = message.from_user.model_dump(include={'user_id', 'first_name'})
    if  User.get(message.from_user.id) is None:
        User.create(id = user_data.get("id") , name = user_data.get("first_name"))
    else:
        await message.answer(f"""Assalomu alaykum {message.from_user.first_name} 🤖
        Tarjimalar Tv Bot - orqali siz o'zingizga yoqqan kinoni topishingiz mumkin 🎬
        Shunchaki kino kodini yuboring va kinoni oling ✅""")


