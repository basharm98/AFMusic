from pyrogram.types import InlineKeyboardButton

import config
from ZeMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᗩᗪᗪ ᗰE TO YOᑌᖇ GᖇOᑌᑭ ˼”", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="«{الدعم}»", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="«{اضفني لمجموعتك}»",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="«{الاوامر}»", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="«ᗪEᐯEᒪOᑭEᖇ ˼”»", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="ᑕᕼᗩᑎᑎEᒪ", url=config.SUPPORT_CHANNEL),
        ],
        [
         
            InlineKeyboardButton(text="ْ𓆩⧛ َ 𝘼َِ𝙁َِ𝙍َِ𝙊َِ𝙊َِ𝙏َِ𝙊ِ ┇ عـ๋͜‏ـۂفــ͡ـࢪتوُ ⧚𓆪", url=f"https://t.me/VVYVVJ"),
        ],
    ]
    return buttons
