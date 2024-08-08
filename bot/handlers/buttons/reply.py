from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def cancel_btn():
    btn = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text='Bekor qilish')]],
        one_time_keyboard=True,
        resize_keyboard=True
    )

    return btn
