from pyrogram import filters
from pyrogram.types import Message

from ZeMusic import app
from ZeMusic.core.call import Mody
from ZeMusic.utils.database import is_music_playing, music_on
from ZeMusic.utils.decorators import AdminRightsCheck
from ZeMusic.utils.inline import close_markup
from config import BANNED_USERS

# تأكد من أن الدالة AdminRightsCheck مستوردة بشكل صحيح
# إذا لم تكن مستوردة بشكل صحيح، قم بإضافة الاستيراد الصحيح هنا

@app.on_message(filters.command(["resume", "كمل"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def resume_com(cli, message: Message, chat_id):
    if await is_music_playing(chat_id):
        return await message.reply_text("الموسيقى قيد التشغيل بالفعل.")
    await music_on(chat_id)
    await Mody.resume_stream(chat_id)
    await message.reply_text("تم استئناف الموسيقى بنجاح.", reply_markup=close_markup())
