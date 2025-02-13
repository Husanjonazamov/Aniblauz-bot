# aiogram  import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from handlers.generate import video_links




@dp.message_handler(lambda message: message.text.startswith('/start '), state='*')
async def handle_link(message: Message, state: FSMContext):
    parts = message.text.split(' ')
    if len(parts) > 1:
        unique_id = parts[1]
        if unique_id in video_links:
            file_id = video_links[unique_id]
            content_type = unique_id.split('_')[0]
            
            if content_type == 'video':
                await bot.send_video(chat_id=message.chat.id, video=file_id)
            elif content_type == 'document':
                await bot.send_document(chat_id=message.chat.id, document=file_id)
            elif content_type == 'photo':
                await bot.send_photo(chat_id=message.chat.id, photo=file_id)
        else:
            await message.reply("Xato havola.")
    else:
        await message.reply("Noto'g'ri format.")
