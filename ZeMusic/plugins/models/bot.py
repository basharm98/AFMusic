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
    try:
        member = await client.get_chat_member(chat_id, user_id)
        if user_id == 5145609515:
             rank = "<a href='tg://user?id={user_id}'>مطور السورس</a>"
        elif user_id == OWNER_ID:
             rank = "<a href='tg://user?id={user_id}'>المطور</a>"
        else:
             rank = italy
    except Exception as e:
        print(e)
        rank = ""

    #await message.reply_text(f"<b>⌯ نعم حبيبي :</b> {italy}\n<b>⌯ انا اسمي القميل :</b> {bot_name} 🥺🙈 {rank}", reply_markup=keyboard)
    await message.reply_text(f"<b>⌯ مرحباً عزيزي :</b> {rank}\n<b>⌯ ما هي الاغنيه التي تريد تشغيلها أو البحث عنها</b>")


