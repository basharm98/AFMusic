import asyncio
from ZeMusic import app 
from strings.filters import command
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


italy = ["عيون عبود",
         "روح عبود",
         "قلب عبود",
         "حب عبود",
         "شتبي مني",
        "زعلان",
        "مريض"]

@app.on_message(filters.text & filters.regex(r"(^|\W)عبود(\W|$)"))
async def Italymusic(client, message):
    if "عبود" in message.text:
        response = random.choice(italy)
        await message.reply(response)
