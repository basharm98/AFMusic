import os, asyncio
from typing import Optional
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from telegraph import upload_file
from ZeMusic import app


#---------------FUNCTION---------------#

def get_file_id(msg: Message) -> Optional[Message]:
    if not msg.media:
        return None

    for message_type in ("photo", "animation", "audio", "document", "video", "video_note", "voice", "sticker"):
        obj = getattr(msg, message_type)
        if obj:
            setattr(obj, "message_type", message_type)
            return obj

#---------------FUNCTION---------------#


@app.on_message(filters.command(["تلغراف", "ميديا", "تلكراف", "تلجراف"]))
async def telegraph_upload(bot, update):
    replied = update.reply_to_message
    if not replied:
        return await update.reply_text("⌯ ¦ قم بالرد على ملف وسائط مدعوم.\n⌯ ¦ حط صوره او فيديو و اكتب عليها.")
    file_info = get_file_id(replied)
    if not file_info:
        return await update.reply_text("⌯ ¦ ياغبي غير مدعوم.\n⌯ ¦ حط صوره و اكتب عليها.")
    text = await update.reply_text(text="<code>انتظر يتم التحميل ...</code>", disable_web_page_preview=True)   
    media = await update.reply_to_message.download()   
    await text.edit_text(text="<code>اكتمل التحميل. الآن يتم رفعه إلى التلغراف ...</code>", disable_web_page_preview=True)                                            
    try:
        response = upload_file(media)
    except Exception as error:
        print(error)
        await text.edit_text(text=f"Error :- {error}", disable_web_page_preview=True)       
        return    
    try:
        os.remove(media)
    except Exception as error:
        print(error)
        return    
    await text.edit_text(
        text=f"<b>تم انشاء الرابط 💞 :-</b>\n\n<code>https://te.legra.ph{response[0]}</code>",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton(text="🎯 ¦ افـتح الـرابـط", url=f"https://te.legra.ph{response[0]}"),
            InlineKeyboardButton(text="♻️ ¦ مشـاركه الـرابـط", url=f"https://telegram.me/share/url?url=https://te.legra.ph{response[0]}")
            ],[
            InlineKeyboardButton(text="✘ اغلاق ✘", callback_data="close")
            ]])
        )
    
