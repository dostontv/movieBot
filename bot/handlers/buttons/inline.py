from aiogram.utils.keyboard import  InlineKeyboardBuilder, InlineKeyboardButton




def book_categori():
    catigori_menu =InlineKeyboardBuilder()
    catigori_menu.add(
        InlineKeyboardButton(text=("") , callback_data="⚡️ IKAR"),
        InlineKeyboardButton(text=("📚 Factor books kit...") ,callback_data="📚 Factor books kit...")
    )
    catigori_menu.button(text="🔍qidirish", switch_inline_query_current_chat="")
    catigori_menu.adjust(2, repeat=True)
    return catigori_menu.as_markup(resize_keyboard=True)