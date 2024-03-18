import asyncio
import os
import time
import requests
from config import START_IMG_URL, OWNER_ID
from pyrogram import filters
import random
from pyrogram import Client, filters, emoji
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import choice, randint

@app.on_message(
  command(["مطور","المطور"])
)
async def devid(client: Client, message: Message):
    dev_id = OWNER_ID 
    info = await app.get_chat(dev_id)
    name = info.first_name
    bio = info.bio
    
    await message.download_media(info.photo.big_file_id, file_name=os.path.join("downloads", "developer.jpg"))    
    await message.reply_photo(
        photo="downloads/developer.jpg",
        caption=f"""<b>⌯ المطور :</b> <a href="tg://user?id={dev_id}">{name}</a>
        
<b>⌯ البايو :</b> {bio}""",
        reply_markup = InlineKeyboardMarkup(
            [
                [ 
                    InlineKeyboardButton(name, user_id=dev_id)
                ]
            ]
        ), 
      )
