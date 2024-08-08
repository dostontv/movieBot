from aiogram.utils.keyboard import InlineKeyboardBuilder


def search_category():
    category_menu = InlineKeyboardBuilder()
    category_menu.button(text="🔍Qidirish", switch_inline_query_current_chat="")
    return category_menu.as_markup()

