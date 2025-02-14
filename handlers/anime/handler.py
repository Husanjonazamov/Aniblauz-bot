# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from utils import texts, buttons
from services.services import getAnime





@dp.message_handler(lambda message: message.text.startswith('/start '), state="*")
async def send_anime(message: Message, state: FSMContext):
    unique_id = message.get_args()
    anime_id = unique_id.replace("anime_", "")

    anime_list = getAnime()
    anime = next((anime for anime in anime_list if str(anime['id']) == anime_id), None)
    
    if anime:
        anime_caption = f"<b>{anime['name']}</b>\n{anime['description']}"
        try:
            await message.answer_video(
                video=anime['anime_id'],
                caption=anime_caption,
            )
        except Exception as e:
            print(f"Hujjatni yuborishda xatolik: {e}")
            await message.reply("Anime faylini yuborishda xatolik yuz berdi.")
    else:
        await message.reply("Kechirasiz, bu anime mavjud emas.")

