# aiogram  import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons
from services.services import getUser, createUser


@dp.message_handler(commands=['start'], state='*')
async def start_handler(message: Message, state: FSMContext):
    
    user_id = message.from_user.id
    user = getUser(user_id)
    
    if user:
        await message.answer(texts.START)
    else:
        name = message.from_user.first_name
        createuser = {
            'name': name,
            'user_id': user_id
        }
        createUser(createuser)
        
        await message.answer(texts.START)

    
                
