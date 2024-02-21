import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["مطور","مطور السورس","مبرمج السورس","المطور"],"")
)
async def huhh(client: Client, message: Message):
    usr = await client.get_users(5145609515)
    f_name = usr.first_name
    l_name = usr.last_name
    usrnam = usr.username
    bio = usr.bio

    full_name = f"{f_name} {l_name}" if l_name else f_name
  
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1a77a02bdb06d55051845.jpg",
        caption=f"""<b>◉ 𝙽𝙰𝙼𝙴 : ❪ [{full_name}](https://t.me/{usrnam}) ❫.\n◉ 𝙸𝙳   : ❪ `5145609515` ❫.\n◉ 𝙱𝙸𝙾  : ❪ {bio} ❫.</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "『 🇾🇪⃤𝐀𝐁𝐃𝐔𝐋𝐋𝐀𝐇 个 ١9 』", url=f"https://t.me/IC_19"), 
                 ],[
                   InlineKeyboardButton(
                        "『 𝚂𝙾𝚄𝚁𝙲𝙴 𝙺𝙸𝙽𝙶 』", url=f"https://t.me/EF_19"),
                ],

            ]

        ),

    )
