from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from ZeMusic import app
from config import Muntazer, OWNER_ID

@app.on_message(filters.private & filters.user(OWNER_ID))
async def must_join_channel(_, message):
    if "‹ قناة الاشتراك ›" in message.text:
        link = f"https://t.me/EF_19"
        await message.reply(
            text=f"~ عزيزي المطور \n~ هذا هي قناة الاشتراك الاجباري @EF_19 .",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("~ 𝙺𝙸𝙽𝙶 .", url=link)]
            ])
        )
