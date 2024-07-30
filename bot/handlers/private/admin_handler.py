from aiogram import Router, F
from aiogram.types import Message

from bot.filters.is_admin_filter import IsAdminFilter

admin_router = Router()


@admin_router.message(IsAdminFilter(), F.video)
async def command_video_handler(message: Message) -> None:
    a = await message.forward('-1002229592627', disable_notification=False)
    await message.answer(f"bazaga qo'shildi {a.message_id}")
