from pyrogram import filters, Client
from ZeMusic import app
import asyncio
from pyrogram.types import VideoChatEnded, Message
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from ZeMusic.core.call import Mody
from ZeMusic.utils.database import *
from pytgcalls.exceptions import (NoActiveGroupCall,TelegramServerError,AlreadyJoinedError)

@app.on_message(filters.regex("^مين في الكول$"))
async def strcall(client, message):
    assistant = await group_assistant(Mody,message.chat.id)
    try:
        await assistant.join_group_call(message.chat.id, AudioPiped("./ZeMusic/assets/call.mp3"), stream_type=StreamType().pulse_stream)
        text="🔔 الاعضاء المتواجدين في الكول :\n\n"
        participants = await assistant.get_participants(message.chat.id)
        k =0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut="يتحدث 🗣 "
            else:
                mut="ساكت 🔕 "
            user = await client.get_users(participant.user_id)
            k +=1
            text +=f"{k}➤{user.mention}➤{mut}\n"
        text += f"\nعددهم : {len(participants)}\n✔️"    
        await message.reply(f"{text}")
        await asyncio.sleep(7)
        await assistant.leave_group_call(message.chat.id)
    except NoActiveGroupCall:
        await message.reply(f"عمووووو الكول مش مفتوح اصلااا\n❌")
    except TelegramServerError:
        await message.reply(f"ارسل الامر تاني في مشكله في سيرفر التلجرام\n❌")
    except AlreadyJoinedError:
        text="🔔 الاعضاء المتواجدين في الكول :\n\n"
        participants = await assistant.get_participants(message.chat.id)
        k =0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut="يتحدث 🗣"
            else:
                mut="ساكت 🔕 "
            user = await client.get_users(participant.user_id)
            k +=1
            text +=f"{k}➤{user.mention}➤{mut}\n"
        text += f"\nعددهم : {len(participants)}\n✔️"    
        await message.reply(f"{text}")
@app.on_message(filters.video_chat_started)
async def brah(client, message):
       await message.reply(" قــام الادمــــن بــفــتــح الــمــحــادثــه الـصـوتـيـه ✓")
@app.on_message(filters.video_chat_ended)
async def brah2(client, message):
       await message.reply("• قــام الادمــــن بـقـفـل الــمــحــادثــه الـصـوتـيـه ✗")
@app.on_message(filters.video_chat_members_invited)
async def fuckoff(client, message):
           text = f"• قــــام ← {message.from_user.mention}"
           x = 0
           for user in message.video_chat_members_invited.users:
             try:
               text += f"\n• بــدعـــوة ←[{user.first_name}](tg://user?id={user.id})"
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text}")
           except:
             pass  
