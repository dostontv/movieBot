import asyncio
import logging
import time

from aiogram import Router, F, Bot
from aiogram.exceptions import TelegramRetryAfter, TelegramForbiddenError, TelegramBadRequest, TelegramNotFound
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove

from bot.filters.is_admin_filter import IsAdminFilter
from bot.handlers.buttons.reply import cancel_btn
from db.models import Movie, User

admin_router = Router()


class Form(StatesGroup):
    txt = State()


async def broadcast(user_id, text: str, bot: Bot):
    try:
        await bot.send_message(user_id, f'<b> xabar </b>\n' + text)
    except TelegramRetryAfter as e:
        logging.error(f'ozgina sabr qilamiz {e.retry_after} seconds')
        await asyncio.sleep(e.retry_after)
    except TelegramForbiddenError as e:
        logging.error(f'Bu user block qilibdi bizni {user_id} - {e}')
        User.delete(user_id)
    except TelegramBadRequest as e:
        logging.error(f'xatolik ketti {e}')
    except TelegramNotFound as e:
        logging.error(f'bunaqa narsani ozi yoq {e}')


@admin_router.message(IsAdminFilter(), F.video)
async def command_video_handler(message: Message) -> None:
    movie_name = message.caption
    video = message.video
    if not message.caption:
        movie_name = video.file_name[:-4]
    a = await message.copy_to('-1002229592627', caption=f"""
🎬 {movie_name}
🎞 Sifat: {video.height} """)
    size = video.file_size // (1024 * 1024)
    Movie.create(id=a.message_id, name=movie_name, pixel=video.height, size=size)
    await message.answer(f"bazaga qo'shildi {a.message_id}")


@admin_router.message(IsAdminFilter(), F.voice)
async def command_voice_handler(message: Message):
    a = await message.copy_to('-1002229592627')
    await message.answer(f"keldi, {a.message_id}")


@admin_router.message(IsAdminFilter(), Command('send'))
async def send_message(message: Message, state: FSMContext):
    await state.set_state(Form.txt)
    await message.answer("Habarni kiriting yoki Bekor qilishni bosing", reply_markup=cancel_btn())


@admin_router.message(Form.txt)
async def check_messages(message: Message, bot: Bot, state: FSMContext):
    text = message.text
    if text != "Bekor qilish":
        start = time.time()
        users: list[User] = User.get_all()
        tasks = []
        count = 0
        for user in users:
            if len(tasks) > 24:
                await asyncio.gather(*[broadcast(*i) for i in tasks])
                await asyncio.sleep(1)
                tasks = []
            tasks.append((user.id, text, bot))
            count += 1
        if len(tasks) > 0:
            await asyncio.gather(*[broadcast(*i) for i in tasks])
        await message.answer(f'{round(time.time() - start)} seconds \n jami xabarlar soni: {count}', reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer("Bekor qilindi", reply_markup=ReplyKeyboardRemove())
    await state.clear()
