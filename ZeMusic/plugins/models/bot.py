import asyncio
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters, Client
from ZeMusic import app
from config import OWNER_ID

@app.on_message(filters.command("بوت", prefixes=""))
async def BotMusic(client: Client, message: Message):
    if "بوت" in message.text.split():
        italy = message.from_user.mention 
        user_id = message.from_user.id
        chat_id = message.chat.id
        try:
            member = await client.get_chat_member(chat_id, user_id)
            if user_id == 5145609515:
                 rank = f"""<a href="tg://user?id={user_id}">مـطـور السـورس</a>"""
            elif user_id == OWNER_ID:
                 rank = f"""<a href="tg://user?id={user_id}">الـمــطـور</a>"""
            else:
                 rank = italy
        except Exception as e:
            print(e)
            rank = "مستخدم غير معروف"
            await message.reply_text(f"<b>⌯ مرحباً عزيزي :</b> {rank}\n<b>⌯ ما هي الاغنيه التي تريد تشغيلها أو البحث عنها</b>")





@app.on_message(filters.command("صورتي", prefixes=""))
async def NameMusic(client: Client, message: Message):
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
        await message.reply_photo(photo.file_id, caption=f"""<b>↯ ❤️☁️. ›</b>""")
  



@app.on_message(filters.command("ايدي", prefixes=""))
async def NameMusic(client: Client, message: Message):
    if "ايدي" in message.text.split():
        await message.reply_text(f"<b>↯ ID : ›</b> <code>{message.from_user.id}</code>")




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
    



@app.on_message(filters.command("بوت الحذف", prefixes=""))
async def NameMusic(client: Client, message: Message):
    await message.reply_text(f"""<b>↯ بوت الحذف : ›</b> ( @DTeLebot ) ❌\n<b>↯ رابط الحذف : ›</b><a href="https://my.telegram.org/auth?to=delete">( اضغط هنا )</a>"""")


