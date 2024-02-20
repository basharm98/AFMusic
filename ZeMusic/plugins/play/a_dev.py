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
                
@app.on_message(filters.command(["عبدالله","عبود","abdullah","abdallah"],"")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1a77a02bdb06d55051845.jpg",
        caption=f"""◉ 𝙸𝙳      : ❪مطور بوت وسورس 𝙺𝙸𝙽𝙶 𝙼𝚄𝚂𝙸𝙲 ❤️🥺❫
◉ 𝙽𝙰𝙼𝙴 : ❪ 『 🇾🇪⃤𝐀𝐁𝐃𝐔𝐋𝐋𝐀𝐇 个 ١9 』 ❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @IC_19 ❫
◉ 𝙱𝙸𝙾    : ❪  حᝳᝲـلـم ᭭ㅤ𓅓  ❫""",
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
