# aiogram  import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from handlers.generate import video_links
from utils import texts



@dp.message_handler(lambda message: message.text.startswith('/start '), state='*')
async def handle_link(message: Message, state: FSMContext):
    parts = message.text.split(' ')
    if len(parts) > 1:
        unique_id = parts[1]
        if unique_id in video_links:
            file_id = video_links[unique_id]
            content_type = unique_id.split('_')[0]
            
            method = None
            data = {
                'chat_id': message.chat.id,
                'protect_content': True
            }
            
            if content_type == 'video':
                method = 'sendVideo'
                data['video'] = file_id
            elif content_type == 'document':
                method = 'sendDocument'
                data['document'] = file_id
            elif content_type == 'photo':
                method = 'sendPhoto'
                data['photo'] = file_id

            if method:
                await bot.request(method, data)
        else:
            await message.reply(texts.NOT_URL)
    else:
        await message.reply(texts.ERROR_URL)
