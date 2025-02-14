from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp





@dp.message_handler(content_types=['video'], state='*')
async def video_handler(message: Message, state: FSMContext):
    video_id = message.video.file_id
    
    await message.answer(video_id)
