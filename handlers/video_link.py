# aiogram  import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from handlers.generate import video_links




@dp.message_handler(lambda message: message.text.startswith('/start video_'), state='*')
async def handle_link(message: Message, state: FSMContext):
    unique_id = message.text.split(' ')[1]
    file_id = video_links[unique_id]
    await bot.send_video(chat_id=message.chat.id, video=file_id)