from aiogram import Router, F
from aiogram.types import Message

from bot.filters.is_admin_filter import IsAdminFilter
from db.models import  Movie

admin_router = Router()


@admin_router.message(IsAdminFilter(), F.video)
async def command_video_handler(message: Message) -> None:
    if message.caption:
        a = await message.copy_to('-1002229592627', disable_notification=False)
        data = message.caption.split('\n')
        Movie.create(id = a.message_id, name = data[0] , pixel =data[1])
        await message.answer(f"bazaga qo'shildi {a.message_id}")

@admin_router.message(IsAdminFilter(), F.voice)
async def command_voice_handler(message: Message):
    a = await message.copy_to('-1002229592627')
    await message.answer(f"keldi,{a.message_id}")
