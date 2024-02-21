import asyncio
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from ZeMusic import app
from telethon.sync import TelegramClient
from telethon.tl.functions.users import GetFullUser

# تعريف معلومات الحساب ومتغيرات أخرى
api_id = "20036317"
api_hash = "986cb4ba434870a62fe96da3b5f6d411"
phone_number = "+967738257380"
session_name = "session_name"
developer_user_id = "5145609515"

@app.on_message(filters.command(["مطور","مطور السورس","مبرمج السورس","المطور"],""))
async def get_developer_info(client, message):
    async with TelegramClient(session_name, api_id, api_hash) as client_telethon:
        # جلب معلومات المطور
        developer = await client_telethon(GetFullUser(developer_user_id))
        # تنسيق البيانات
        caption = f"◉ 𝙽𝙰𝙼𝙴 : {developer.user.first_name}\n" \
                  f"◉ 𝚄𝚂𝙴𝚁 : @{developer.user.username}\n" \
                  f"◉ 𝙱𝙸𝙾  : {developer.about}"
        # إرسال الصورة والبيانات كرد على الرسالة الأصلية
        await message.reply_photo(
            photo=await client_telethon.download_profile_photo(developer.user),
            caption=caption,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "『 🇾🇪⃤𝐀𝐁𝐃𝐔𝐋𝐋𝐀𝐇 个 ١9 』", url="https://t.me/IC_19"), 
                     ],[
                       InlineKeyboardButton(
                            "『 𝚂𝙾𝚄𝚁𝙲𝙴 𝙺𝙸𝙽𝙶 』", url="https://t.me/EF_19"),
                    ],
                ]
            )
        )
