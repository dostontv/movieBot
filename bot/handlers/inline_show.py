from aiogram import Router
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent


inline_show_router = Router()

books = [
    {
        "id": 1,
        "name": "Ikki dunyo",
        "image": "https://telegra.ph/file/a7d72d0c776605249fe51.png",
        "author": "uzbekistan",
        "price": 150000,
    },
    {
        "id": 2,
        "name": "Oq kema",
        "image": "https://telegra.ph/file/d438ec818cb3dcd460243.png",
        "author": "uzbekistan",
        "price": 100000,
    },
    {
        "id": 3,
        "name": "Pycharm Book",
        "image": "https://telegra.ph/file/feab6d06b25dc6231e686.png",
        "author": "uzbekistan",
        "price": 1000000,
    },
    {
        "id": 4,
        "name": "Docker",
        "image": "https://telegra.ph/file/48a817e55b67756572ed0.png",
        "author": "uzbekistan",
        "price": 1200000,
    }
]


@inline_show_router.inline_query()
async def show_product(inline_query: InlineQuery):
    result = []
    if len(inline_query.query) >= 2:
        for book in books:
            tmp = InlineQueryResultArticle(
                id = str(book["id"]),
                title= book["name"],
                description=str(f"P20 books\n💴 Narxi: {book['price']} so'm"),
                thumbnail_url=book["image"],
                input_message_content= InputTextMessageContent(message_text=book["name"])
            )
            result.append(tmp)

        await inline_query.answer(result, cache_time=5, is_personal=True)

