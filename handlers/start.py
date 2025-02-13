# aiogram  import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons





@dp.message_handler(commands=['start'], state='*')
async def start_handler(message: Message, state: FSMContext):
    
    first_name = message.from_user.first_name
    
    await message.answer(texts.START.format(first_name))
