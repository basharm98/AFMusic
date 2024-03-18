import asyncio
import os
from pyrogram import filters
from pyrogram import Client, emoji
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from strings.filters import command
from ZeMusic import app
from config import OWNER_ID

@app.on_message(
    command(["مطور","المطور"])
)
async def devid(client: Client, message: Message):
    info = await client.get_users(OWNER_ID)
    name = info.first_name
    bio = info.bio
    
    await message.download_media(info.photo.big_file_id, file_name=os.path.join("downloads", "developer.jpg"))    
    await message.reply_photo(
        photo="downloads/developer.jpg",
        caption=f"""<b>⌯ المطور :</b> <a href="tg://user?id={dev_id}">{name}</a>
        
<b>⌯ البايو :</b> {bio}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [ 
                    InlineKeyboardButton(name, user_id=dev_id)
                ]
            ]
        ), 
    )
