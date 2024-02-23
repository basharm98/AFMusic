import asyncio
import telebot

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

#          
                
@app.on_message(filters.command(["مطور","مطور السورس","مبرمج السورس","المطور"],"")
)
async def huhh(client: Client, message: Message):
    msg_text = message.text
    if (
        msg_text in ["المطور", "مطور"]
    ):
        
        def Mrk():
            mrk = InlineKeyboardMarkup()
            btn = InlineKeyboardButton(
                text=chan_inf.title if chan_inf.title else chan_inf.first_name,
                url="https://t.me/" + chan_inf.username,
            )
            mrk.add(btn)
            return mrk

        # استخدم المعرف "5145609515" لجلب معلومات المستخدم
        bio = bot.get_chat(5145609515)
        Photo_user = f"https://t.me/{bio.username}"
        ttxt = f"""✯︙𝙽𝙰𝙼𝙴 : {bio.first_name}
✯︙𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 : @{bio.username}
✯︙𝙸𝙳 : {bio.id} .
✯︙𝙱𝙸𝙾 :  {bio.bio}) ."""
        try:
            await message.reply_photo(
                photo=Photo_user,
                caption=ttxt,
                reply_markup=Mrk(),
            )
        except:
            await message.reply_text(
                text=ttxt,
                reply_markup=Get_prerson(name=bio.first_name, id=bio.id),
            )
