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
    command(["سورس","‹ السورس ›","king","السورس", "سورس كينج","سورس king"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1a77a02bdb06d55051845.jpg",
        caption=f"""╭────── • ◈ • ──────╮

   <b>么 ⌯ 𝚂𝙾𝚄𝚁𝙲𝙴</b> (t.me/EF_19)
   <b>么 ⌯ 𝙳𝙴ꪜ</b>    (t.me/IC_19)

╰────── • ◈ • ──────╯
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "‹  ᦔꫀꪜ ꪖᠻ𝘳ꪮ𝓽ꪮꪮ . 🕷 › ", url=f"https://t.me/IC_19"),
                ],[
                    InlineKeyboardButton(
                        "‹ ᥴ𝗁ᥲ️ꪀꪀᥱᥣ›", url=f"https://t.me/EF_19"), 
                    InlineKeyboardButton(
                        "‹ ᥉υρρ᥆ᖇƚ›", url=f"https://t.me/GY_19"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف البوت لمجموعتك ›", url=f"https://t.me/A_Rn_obot?startgroup=true"),
            ]
        ]
         ),
     )
  
