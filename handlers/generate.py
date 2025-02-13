# aiogram  import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils.env import BOT_URL
from utils import texts

video_links = {}
ADMIN = 6415392394


@dp.message_handler(content_types=['video', 'document', 'photo'], state='*')
async def start_handler(message: Message, state: FSMContext):

    if message.from_user.id == ADMIN:
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
            unique_id = f"{content_type}_{len(video_links) + 1}"
            video_links[unique_id] = file_id

            video_url = f"{BOT_URL}?start={unique_id}"
            await message.answer(video_url)
    else:
        await message.answer(texts.NOT_ADMIN)
        
