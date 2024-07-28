from aiogram import Router, Bot, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from db.models import User

main_router = Router()


@main_router.message(CommandStart())
async def command_start_handler(message: Message, bot: Bot) -> None:
    user = message.from_user
    if  User.get(message.from_user.id) is None:
        User.create(id = user.id , name = user.full_name)
    else:
        await message.answer(f"""Assalomu alaykum {message.from_user.first_name} 🤖
CineBot - orqali siz o'zingizga yoqqan kinoni topishingiz mumkin 🎬
Shunchaki kino kodini yoki qidirish bo'limidan kino nomi yoki janiri yuboring va kinoni oling ✅""")



@main_router.message(F.text.isdigit())
async def command_isdigit(message : Message):
    await  message.answer('buraqam')








