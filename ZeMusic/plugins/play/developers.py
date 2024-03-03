import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client, filters, emoji
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

from pyrogram.types import ChatMemberUpdated
#          
                
@app.on_message(filters.command(["مطور","مطور السورس","مبرمج السورس","المطور"],"")
)
async def huhh(client: Client, message: Message):
    dev_id = 5145609515
    info = await app.get_chat(dev_id)
    name = info.first_name
    bio = info.bio

    await app.download_media(info.photo.big_file_id, file_name=os.path.join("downloads", "developer.jpg"))     
    await message.reply_photo(
        photo="downloads/developer.jpg",
        caption=f"<b>◉ 𝙽𝙰𝙼𝙴 : ❪ 🇾🇪⃤𝐀𝐁𝐃𝐔𝐋𝐋𝐀𝐇 个 ١9 ❫</b>
<b>◉ 𝙸𝙳   : ❪ 5145609515 ❫</b>
<b>◉ 𝚄𝚂𝙴𝚁 : ❪ @IC_19 ❫</b>
◉ 𝙱𝙸𝙾  : {bio}",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "『 🇾🇪⃤𝐀𝐁𝐃𝐔𝐋𝐋𝐀𝐇 个 ١9 』", url=f"https://t.me/IC_19"), 
                 ],[
                   InlineKeyboardButton(
                        "『 𝙺𝙸𝙽𝙶 𝚂𝙾𝚄𝚁𝙲𝙴 』", url=f"https://t.me/EF_19"),
                ],

            ]

        ),

    )
