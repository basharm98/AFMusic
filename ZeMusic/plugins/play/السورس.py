import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint
import config
                
@app.on_message(
    command(["سورس","‹ السورس ›"," ","السورس"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/17382ddaaaba35c95d4c4.jpg",
        caption = f"""<b>  ⌯ 𝚆𝙴𝙻𝙲𝙾𝙼𝙴 𝚃𝙾 . .<br>
        <a href="https://t.me/EF_19"> ⌯ 𝚂𝙾𝚄𝚁𝙲𝙴 𝙺𝙸𝙽𝙶 ⛧</a></b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="‹ لتنصيب بوت ›", url=f"https://t.me/S_SC7"),
                ],[
                    InlineKeyboardButton(
                        text=config.SURS_NAME, url=config.SUPPORT_CHANNEL),
                ],

            ]

        ),

    )
