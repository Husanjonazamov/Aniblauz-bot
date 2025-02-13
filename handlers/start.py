# aiogram  import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons
from utils.env import ADMIN



@dp.message_handler(commands=['start'], state='*')
async def start_handler(message: Message, state: FSMContext):
    
    user_id = message.from_user.id
    
    if user_id == ADMIN:
        await message.answer(texts.START_ADMIN)
    else:
        await message.answer(texts.START)
        
                
