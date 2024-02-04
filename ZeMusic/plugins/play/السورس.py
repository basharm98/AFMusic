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

                
@app.on_message(
    command(["سورس","‹ السورس ›","عفرتو","السورس", "سورس عفرتو"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/04b2f1f1c808dc49db35b.jpg",
        caption=f"""**ᯓ 𝚆𝙴𝙻𝙲𝙾𝙼𝙴 𝚃𝙾 𝚂𝙾𝚞𝚁𝚂 𝙰𝙵𝚁𝙾𝚃𝙾𝙾](https://t.me/UI_VM)**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "{مطور السورس}", url=f"https://t.me/IIUll_l"), 
                    
                
                    InlineKeyboardButton(
                        "‹{ الدعم } ›", url=f"https://t.me/T_Y_E_X"),
                ],[
                    
                
                    InlineKeyboardButton(
                        "‹ { السورس } ›", url=f"https://t.me/UI_VM"),
                
        ],

            ]

        ),

    )

