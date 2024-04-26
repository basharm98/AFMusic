import asyncio
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters, Client
from ZeMusic import app
from config import OWNER_ID

@app.on_message(filters.command("بوت", prefixes=""))
async def BotMusic(client: Client, message: Message):
    italy = message.from_user.mention 
    user_id = message.from_user.id
    chat_id = message.chat.id
    await message.reply_text(f"<b>⌯ مرحباً عزيزي :</b> {rank}\n<b>⌯ ما هي الاغنيه التي تريد تشغيلها أو البحث عنها</b>")




@app.on_message(filters.command("ايدي", prefixes=""))
async def NameMusic(client: Client, message: Message):
    await message.reply_text(f"<b>↯ ID : ›</b> <u>{message.from_user.id}</u>")




@app.on_message(filters.command("اسمي", prefixes=""))
async def NameMusic(client: Client, message: Message):
    await message.reply_text(f"<b>↯ اسمك : ›</b> {message.from_user.mention}")




@app.on_message(filters.command("يوزري", prefixes=""))
async def UserMusic(client: Client, message: Message):
    await message.reply_text(f"<b>↯ يوزرك : ›</b> @{message.from_user.username}")




@app.on_message(filters.command("البايو", prefixes=""))
async def BioMusic(client: Client, message: Message):
    usr = await client.get_chat(message.from_user.id)
    bio = usr.bio
    await message.reply_text(f"""<b>↯ البايو : ›</b> {bio}""")
    
