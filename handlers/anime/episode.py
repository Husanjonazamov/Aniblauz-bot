# aiogram import
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext


# kode import
from loader import dp, bot
from utils import texts, buttons
from services.services import getEpisode
from utils.env import BOT_TOKEN
import requests



@dp.callback_query_handler(lambda c: c.data.startswith('anime_'))
async def process_callback(callback_query: CallbackQuery, state: FSMContext):
    anime_id = callback_query.data.split('_')[1]
    episodes = getEpisode(anime_id)
    
    if episodes:
        for episode in episodes:
            name = episode['name']
            description = episode['description']
            episode_id = episode['episode_id']
            
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendVideo"
            
            chat_id = callback_query.message.chat.id
            
            data = {
                'chat_id': chat_id,
                'video': episode_id,
                'caption': texts.anime_text(name=name, description=description),
                'parse_mode': 'HTML',
                'protect_content': True
            }
            
            response = requests.post(url, data=data)    
    else:
        await callback_query.message.answer(texts.NOT_EPISODE)
