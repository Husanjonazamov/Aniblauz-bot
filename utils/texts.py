START_ADMIN = \
"""
📁 <b>Faylni yuboring (video, hujjat yoki foto)</b>
"""

START = \
"""
👋 <b>Assalomu alaykum</b>
"""

NOT_ADMIN = \
"""
🚫 <b>Sizda bu amalni bajarish uchun ruxsat yo'q.</b>
"""

NOT_URL = \
"""
❌ <b>Havola xato</b>
"""

EXPIRED_URL = \
"""
⏳ <b>Bu havola eskirgan</b>
""" 


NOT_ANIME = \
"""
Kechirasiz, bu anime mavjud emas.
"""


ERROR_ANIME = \
"""
<b>Anime videosini yuborishda xatolik yuz berdi.</b>
"""





ALL_ANIME_DOWNLOAD = \
"""
Hammasini yuklab olasizmi
"""



NOT_EPISODE = \
"""
Epizodlar topilmadi.
"""


def anime_text(**kwargs):
    anime = ''
    
    anime += f"<b>{kwargs['name']}</b>\n"
    anime += f"<b>{kwargs['description']}</b>"
    
    return anime    