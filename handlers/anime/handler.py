# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
import requests

from loader import dp
from services.services import getAnime
from utils.env import BOT_TOKEN
from utils import texts




@dp.message_handler(lambda message: message.text.startswith('/start '), state="*")
async def send_anime(message: Message, state: FSMContext):
    unique_id = message.get_args()
    anime_id = unique_id.replace("anime_", "")

    anime_list = getAnime()
    anime = next((anime for anime in anime_list if str(anime['id']) == anime_id), None)
    
    if anime:
        anime_caption = f"<b>{anime['name']}</b>\n{anime['description']}"
        chat_id = message.chat.id
        video_id = anime['anime_id']
        
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendVideo"
        data = {
            'chat_id': chat_id,
            'video': video_id,
            'caption': anime_caption,
            'parse_mode': 'HTML',
            'protect_content': True
        }
        
        response = requests.post(url, data=data)
        
        if response.status_code != 200:
            await message.reply(texts.ERROR_ANIME)
    else:
        await message.reply(texts.NOT_ANIME)
