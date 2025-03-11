from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from loader import dp



ADMINS= [5765144405,1229568290,7691756537]



@dp.message_handler(content_types=['video'], state='*')
async def video_handler(message: Message, state: FSMContext):
    
    if message.from_user.id in ADMINS:
        video_id = message.video.file_id
        await message.answer(video_id)
