from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# Kode import
from loader import dp, bot
from utils.env import BOT_URL, ADMIN, BOT_ADMIN
from utils import texts
import json


ADMINS = [ADMIN, BOT_ADMIN]

VIDEO_LINKS_FILE = 'video_links.json'

def load_links():
    try:
        with open(VIDEO_LINKS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_links(links):
    with open(VIDEO_LINKS_FILE, 'w') as f:
        json.dump(links, f)

video_links = load_links()

@dp.message_handler(content_types=['video', 'document', 'photo'], state='*')
async def start_handler(message: Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        file_id = None
        content_type = None
        
        if message.video:
            file_id = message.video.file_id
            content_type = 'video'
        elif message.document:
            file_id = message.document.file_id
            content_type = 'document'
        elif message.photo:
            file_id = message.photo[-1].file_id
            content_type = 'photo'
        
        if file_id and content_type:
            count = sum(1 for key in video_links if key.startswith(content_type))
            unique_id = f"{content_type}_{count + 1}"
            video_links[unique_id] = file_id
            save_links(video_links)

            video_url = f"{BOT_URL}?start={unique_id}"
            await message.answer(video_url)
    else:
        await message.answer(texts.NOT_ADMIN)
