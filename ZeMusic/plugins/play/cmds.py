import asyncio
import os
import requests
import pyrogram
from pyrogram import Client, filters, emoji
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified
from ZeMusic import app
from config import OWNER_ID, LOGGER_ID


@app.on_message(filters.command(["مطور", "المطور"]) & filters.group)
async def zilzal(client: Client, message: Message):
    usr = await client.get_users(OWNER_ID)
    name = usr.first_name
    usrnam = usr.username
    async for photo in client.iter_profile_photos(OWNER_ID, limit=1):
        await message.reply_photo(
            photo.file_id,
            caption=f"""ٴ<b>•────‌‌‏✯ ʑ_ᴍᴜsɪᴄ ✯──‌‌‏─‌‌‏─•</b>
            
- 𝚆𝙾𝙽𝙴𝚁 :[{usr.first_name}](https://t.me/{usrnam})
- 𝚄𝚂𝙴𝚁 :@{usrnam} 
- 𝙸𝙳 :`{usr.id}`
 
ٴ<b>•────‌‌‏✯ ʑ_ᴍᴜsɪᴄ ✯──‌‌‏─‌‌‏─•</b> """,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(name, url=f"https://t.me/{usrnam}")],
                    [InlineKeyboardButton("•✯ ᴢᴛʜᴏɴ_ᴍᴜsɪᴄ ✯•", url="https://t.me/EF_19")],
                ]
            )
        )
        
    sender_id = message.from_user.id
    sender_name = message.from_user.first_name
    senderuser = message.from_user.username
    sender_user = f"@{senderuser}" if senderuser else "لا يوجد"
    await app.send_message(OWNER_ID, f"- المستخدم {message.from_user.mention} يناديـك \n\n- الاسـم : {sender_name} \n- الايـدي : {sender_id}\n- اليـوزر : {sender_user}")
    await app.send_message(LOGGER_ID, f"- المستخـدم {message.from_user.mention} يناديـك \n\n- الاسـم : {sender_name} \n- الايـدي : {sender_id}\n- اليـوزر : {sender_user}")
