import asyncio
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters, Client
from ZeMusic import app
from config import OWNER_ID

@app.on_message(filters.command(["بوت"], prefixes=""))
async def ZeMusic(client: Client, message: Message):
    me = await client.get_me()
    bot_username = me.username
    bot_name = me.first_name
    italy = message.from_user.mention
    button = InlineKeyboardButton("اضف البوت الي مجموعتك🏅", url=f"https://t.me/{bot_username}?startgroup=true")
    keyboard = InlineKeyboardMarkup([[button]])
    user_id = message.from_user.id
    chat_id = message.chat.id
    try:
        member = await client.get_chat_member(chat_id, user_id)
        if user_id == 5145609515:
             rank = "مالك ومطور السورس 🥺🫶🏻"
        elif user_id == OWNER_ID:
             rank = " مالك الـبوت 🥺❤️"
        elif member.status == "administrator":
             rank = " الادمــن "
        else:
             rank = "للاسف انت عضو 🥺💔"
    except Exception as e:
        print(e)
        rank = "مش عرفنلو مله ده😒"
    await message.reply_text(
        text=f"""⌯ نعم حبيبي : {italy} 🥰❤️\n⌯ انا اسمي : {bot_name} 🥺🙈\n⌯ رتبتك هي : {rank}""", reply_markup=keyboard)
