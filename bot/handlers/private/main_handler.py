from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from db.models import User, Movie

main_router = Router()


@main_router.message(F.text.isdigit())
async def command_isdigit(message: Message):
    movie = Movie.get(int(message.text))
    if not movie:
        await message.answer("Kino topilmadi")
    else:
        await message.answer(movie.name)


@main_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    user = message.from_user
    if not User.get(message.from_user.id):
        User.create(id=user.id, name=user.full_name)
    await message.answer(f"""Assalomu alaykum {user.first_name} 🤖
CineBot - orqali siz o'zingizga yoqqan kinoni topishingiz mumkin 🎬
Shunchaki kino kodini yoki qidirish bo'limidan kino nomi yoki janiri yuboring va kinoni oling ✅""")
