from aiogram.utils.keyboard import  InlineKeyboardBuilder, InlineKeyboardButton




def search_categori():
    catigori_menu =InlineKeyboardBuilder()
    catigori_menu.button(text="🔍qidirish", switch_inline_query_current_chat="")
    return catigori_menu.as_markup(resize_keyboard=True)