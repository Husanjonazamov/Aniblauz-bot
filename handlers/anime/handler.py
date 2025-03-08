from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# Kod importlari
import requests

from loader import dp
from services.services import getAnime, getEpisodesList, getEpisode
from utils.env import BOT_TOKEN
from utils import texts, buttons



@dp.message_handler(lambda message: message.text.startswith('/start '), state="*")
async def send_anime_or_episode(message: Message, state: FSMContext):
    unique_id = message.get_args()
    anime_id = unique_id.replace("anime_", "")

    anime_list = getAnime()
    episode_list = getEpisodesList()
    episode = getEpisode(anime_id)


    anime = next((anime for anime in anime_list if str(anime.get('id')) == anime_id), None)

    if anime:
        name = anime['name']
        description = anime.get('description', '')
        anime_caption = texts.anime_text(name=name, description=description)
        chat_id = message.chat.id
        video_id = anime['anime_id']

        episodes_for_anime = [episode for episode in episode_list if str(episode.get('anime_id')) == anime_id]
        episode_names = "\n".join([episode['name'] for episode in episodes_for_anime]) if episodes_for_anime else "No episodes found."

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendVideo"
        data = {
            'chat_id': chat_id,
            'video': video_id,
            'caption': f"{anime_caption}",
            'parse_mode': 'HTML',
            'protect_content': True
        }
        response = requests.post(url, data=data)

        if response.status_code == 200:
            if episode:
                await message.answer(
                    texts.ALL_ANIME_DOWNLOAD,
                    reply_markup=buttons.create_download_button(anime_id)
                )
            else:
                return
        else:
            await message.reply(texts.ERROR_ANIME)
    else:
        episode_anime = next((ep for ep in episode_list if str(ep.get('id')) == anime_id), None)

        try:
            if episode_anime:
                episode_name = episode['name']
                episode_description = episode.get('description', '')
                episode_caption = f"{episode_name}\n{episode_description}"
                chat_id = message.chat.id
                video_id = episode['episode_id']

                url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendVideo"
                data = {
                    'chat_id': chat_id,
                    'video': video_id,
                    'caption': episode_caption,
                    'parse_mode': 'HTML',
                    'protect_content': True
                }
                response = requests.post(url, data=data)
            else:
                await message.reply(texts.NOT_ANIME_OR_EPISODE)
        except Exception as e:
            print(e)