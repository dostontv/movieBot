from aiogram import Router
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent

from db.models import Movie

inline_show_router = Router()


@inline_show_router.inline_query()
async def show_product(inline_query: InlineQuery):
    result = []
    movies: list[Movie] = Movie.get_all()
    for movie in movies:
        tmp = InlineQueryResultArticle(
            id=str(movie.id),
            title=movie.name,
            description=f'{movie.description} {movie.pixel}',
            thumbnail_url='https://www.postsessionpodcast.com/wp-content/uploads/2021/04/Movies-small.jpg',
            input_message_content=InputTextMessageContent(message_text=str(movie.id))
        )
        result.append(tmp)

    await inline_query.answer(result, cache_time=5, is_personal=True)
