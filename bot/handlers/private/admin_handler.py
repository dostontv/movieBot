from aiogram import Router, F
from aiogram.types import Message

from bot.filters.is_admin_filter import IsAdminFilter
from db.models import Movie

admin_router = Router()


@admin_router.message(IsAdminFilter(), F.video)
async def command_video_handler(message: Message) -> None:
    data = message.caption.split('\n')
    if message.caption and len(data) >1:
        a = await message.copy_to('-1002229592627', disable_notification=False)
        file_size_bytes = message.video.file_size
        file_size_mb = file_size_bytes / 1048576
        Movie.create(id=a.message_id, name=message.video.file_name, pixel=data[1] , size =file_size_mb)
        await message.answer(f"bazaga qo'shildi {a.message_id}")

@admin_router.message(IsAdminFilter(), F.voice)
async def command_voice_handler(message: Message):
    a = await message.copy_to('-1002229592627')
    await message.answer(f"keldi,{a.message_id}")



