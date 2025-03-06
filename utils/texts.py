START_ADMIN = \
"""
📁 <b>Faylni yuklash uchun, iltimos, video, hujjat yoki surat yuboring.</b>
"""

START = \
"""
👋 <b>Assalomu alaykum! Anime olamiga xush kelibsiz!</b>
"""

NOT_ADMIN = \
"""
🚫 <b>Kechirasiz, sizda bu amalni bajarish uchun ruxsat yo'q.</b>
"""

NOT_URL = \
"""
❌ <b>Xato! Havola to'g'ri emas.</b>
"""

EXPIRED_URL = \
"""
⏳ <b>Kechirasiz, bu havola eskirgan.</b>
""" 

NOT_ANIME = \
"""
😔 <b>Kechirasiz, bu anime mavjud emas.</b>
"""

ERROR_ANIME = \
"""
⚠️ <b>Anime videosini yuborishda xatolik yuz berdi. Iltimos, keyinroq yana urinib ko'ring.</b>
"""

ALL_ANIME_DOWNLOAD = \
"""
📥 <b>Hammasini yuklab olmoqchimisiz?</b>
"""

NOT_EPISODE = \
"""
🔍 <b>Epizodlar topilmadi. Yana bir bor tekshiring.</b>
"""

def anime_text(**kwargs):
    anime = ''
    
    anime += f"<b>{kwargs['name']}</b>\n"
    anime += f"<b>{kwargs['description']}</b>"
    
    return anime    


NOT_ANIME_OR_EPISODE = \
"""
😔 <b>Kechirasiz, bu anime mavjud emas.</b>
"""