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
    us_id = OWNER_ID  # استخدام قيمة OWNER_ID من ملف config.py

    # احصل على معلومات المطور باستخدام الايدي المحدد
    developer_info = await client.get_users([us_id])  # قم بتمرير الايدي كقائمة واحدة

    await message.reply_photo(
        photo=developer_info[0].photo.big_file_id,  # الحصول على الصورة من العنصر الأول في القائمة
        caption=f"""<b>⌯ المطور :</b> <a href="tg://user?id={us_id}">{developer_info[0].first_name}</a>
        
<b>⌯ معرف المطور :</b> @{developer_info[0].username}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "المطور", url=f"https://t.me/{developer_info[0].username}"), 
                 ],
            ]
        ),
    )
