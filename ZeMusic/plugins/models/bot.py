import asyncio
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters, Client
from ZeMusic import app
from config import OWNER_ID

@app.on_message(filters.command("بوت", prefixes=""))
async def BotMusic(client: Client, message: Message):
    if "بوت" not in message.text.split():
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
        await message.reply_text(f"<b>⌯ مرحباً عزيزي :</b> {rank}\n<b>⌯ ما هي الاغنيه التي تريد تشغيلها أو البحث عنها</b>")
    else:
        await message.reply_text(f"""<b>↯ بوت الحذف : ›</b> ( @DTeLebot ) ❌\n<b>↯ رابط الحذف : ›</b><a href="https://my.telegram.org/auth?to=delete">( اضغط هنا )</a>""")

        



@app.on_message(filters.command("صورتي", prefixes=""))
async def PiMusic(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    await app.download_media(usr.photo.big_file_id, file_name=os.path.join("downloads", "developer.jpg")) 
    await message.reply_photo(photo="downloads/developer.jpg", caption=f"""<b>↯ ❤️☁️. ›</b>""")
  



@app.on_message(filters.command("ايدي", prefixes=""))
async def IdMusic(client: Client, message: Message):
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
    



@app.on_message(filters.command("بوت1 الحذف", prefixes=""))
async def DeletMusic(client: Client, message: Message):
    await message.reply_text(f"""<b>↯ بوت الحذف : ›</b> ( @DTeLebot ) ❌\n<b>↯ رابط الحذف : ›</b><a href="https://my.telegram.org/auth?to=delete">( اضغط هنا )</a>""")


