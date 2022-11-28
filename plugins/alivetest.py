#delete this afterwards

from pyrogram import Client, filters, __version__ as pyrogram_version
import random 
from telethon import __version__ as telethon_version
from telegram import __version__ as ptbver
import time
StartTime = time.time()
from pyrogram.types import Message
from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from info import SUPPORT_CHAT, BOT_USERNAME
from pyrogram.types import CallbackQuery

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time


@Client.on_message(filters.command("stalive"))
async def alive(_, m: Message):
    user = m.from_user
    uptime = get_readable_time((time.time() - StartTime))
    msg = await m.reply_text("Initialising")
    await msg.edit("Initialising ✪●●●●●")
    time.sleep(1)
    await msg.edit("Initialising ✪✪●●●●")
    time.sleep(1)
    await msg.edit("Initialising ✪✪✪●●●")
    time.sleep(1)
    await msg.edit("Initialising ✪✪✪✪●●")
    time.sleep(1)
    await msg.edit("Initialising ✪✪✪✪✪●")
    time.sleep(1)
    await msg.edit("Initialising ✪✪✪✪✪✪")
    time.sleep(1)
    await msg.edit("✪︎Connection Successful✪")
    pm_caption = f"** ♡ Hey [{user.first_name}](tg://user?id={user.id}) \nI,m Sakura ✨ **\n\n"
    pm_caption += f"**♡ My Uptime :** `{uptime}`\n\n"
    pm_caption += f"**♡ Telethon Version :** `{telethon_version}`\n\n"
    pm_caption += f"**♡ Pyrogram Version :** `{pyrogram_version}`\n\n"
    pm_caption += f"**♡ PTB Version :** `{ptbver}`\n\n"
    pm_caption += "**♡ My Master :** [Amal Nath](https://t.me/Unni0240) "
    await msg.edit_text(text=(pm_caption),disable_web_page_preview=True)

           
