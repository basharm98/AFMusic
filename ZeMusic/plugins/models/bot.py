import asyncio
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters, Client
from ZeMusic import app
from config import OWNER_ID

@app.on_message(filters.command("بوت", prefixes=""))
async def ZeMusic(client: Client, message: Message):
    italy = message.from_user.mention 
    user_id = message.from_user.id
    chat_id = message.chat.id
    await message.reply_text(f"<b>⌯ مرحباً عزيزي :</b> {rank}\n<b>⌯ ما هي الاغنيه التي تريد تشغيلها أو البحث عنها</b>")


