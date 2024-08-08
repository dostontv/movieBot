from aiogram import Router
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent

from bot.handlers.utils import to_latin
from db.models import Movie

inline_show_router = Router()


@inline_show_router.inline_query()
async def show_product(inline_query: InlineQuery):
    result = []
    data = inline_query.query
    if not inline_query.query.isascii():
        data = to_latin(inline_query.query)
    movies: list[Movie | tuple] = Movie.get_all_movies(data)
    for movie in movies:
        if movie is tuple:
            movie = Movie(*movie)

        tmp = InlineQueryResultArticle(
            id=str(movie.id),
            title=f'📽 {movie.name} || {movie.pixel}',
            description=f'💾 Hajmi {movie.size} MB',
            thumbnail_url='https://telegra.ph/file/cd45c7ac765e805b851e7.png',
            input_message_content=InputTextMessageContent(message_text=str(movie.id))
        )
        result.append(tmp)
    else:
        result.append(
            InlineQueryResultArticle(
                id=str(float('inf')),
                title='Boshqa hech nima topilmadi',
                description='Iltimos qayta tekshirib yozing',
                thumbnail_url='https://telegra.ph/file/c17eba3a1410297cb9a33.png',
                input_message_content=InputTextMessageContent(message_text='hech nima topilmadi')
            )
        )
    await inline_query.answer(result, cache_time=5, is_personal=True)
