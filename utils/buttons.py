from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_download_button(anime_id):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='Barchasini yuklab olish', 
                    callback_data=f"anime_{anime_id}"
                )
            ]
        ]
    )
