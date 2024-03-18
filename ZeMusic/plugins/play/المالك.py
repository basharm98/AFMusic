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
    usr = await client.get_users(OWNER_ID)
    name = usr.first_name
    usrnam = usr.username
    
    await message.reply_photo(
        photo="https://telegra.ph/file/1a77a02bdb06d55051845.jpg",
        caption=f"""<b>⌯ المطور :</b> {message.from_user.mention}
        
<b>⌯ البايو :</b> ح‍‌ل‍‌م‍‌ ☻🥂.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [ 
                    InlineKeyboardButton(name, url=f"https://t.me/{usrnam}"),
                ]
            ]
        ), 
    )
