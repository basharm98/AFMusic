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

#          
                
def Identification_(message: Message):
    user_ = message.from_user
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
            bot.send_photo(
                Photo_user,
                reply_to_message_id=message.id,
                caption=ttxt,
                reply_markup=Mrk(),
            )
        except:
            bot.send_message(
                ttxt,
                reply_to_message_id=message.id,
                reply_markup=Get_prerson(name=bio.first_name, id=bio.id),
            )

