from aiogram.dispatcher.filters.state import StatesGroup, State




class VideoGenerateState(StatesGroup):
    video = State()