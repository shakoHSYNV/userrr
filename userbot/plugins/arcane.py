import os
import time
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import ALIVE_NAME, StartTime, CMD_HELP
from userbot.legend import BOT
from userbot.utils import admin_cmd, sudo_cmd
from telethon import version
from math import ceil
import json
import random
import re
from telethon import events, errors, custom
import io
from platform import python_version, uname

ALIVE_PHOTTO = "https://telegra.ph/file/f71f9b1cbd6459391d422.mp4"


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "π°ππ²π°π½π΄"

global ghanti
        
#make by LEGEND X bht mehnat lag gayi yrr but banhi gaya π           
#@command(outgoing=True, pattern="^.arcane$")
@borg.on(admin_cmd(pattern=r"awake"))
async def amireallyalive(awake):
   """ For .arcane command, check if the bot is running or not.  """
   tag = borg.uid
   uptm = await legend.get_readable_time((time.time() - StartTime))
   ALIVE_MESSAGE= f" ΰΌοΈ {BOT} ΰΌοΈ π°πΊ πΌπ· π¨π΅π« πΉπ¬π¨π«π π»πΆ πΊπ¬πΉπ½π¬ ππΆπΌβ.  "
   ALIVE_MESSAGE += "\n\n"
   ALIVE_MESSAGE += "ΰΌ πππππ΄πΌ πππ°πππ ΰΌ\n\n"
   ALIVE_MESSAGE += "π£ ππ΄π»π΄ππ·πΎπ½ ππ΄πππΈπΎπ½ π£ : 1.19.5\n\n"
   ALIVE_MESSAGE += "β π°ππ²π°π½π΄ ππ΄πππΈπΎπ½ β :   0.1\n\n"
   ALIVE_MESSAGE += f"π£ ππΏππΈπΌπ΄ π£ : {uptm}\n\n"
   ALIVE_MESSAGE += f"κ§ πΌπ π±πΎππ κ§: [{DEFAULTUSER}](tg://user?id={tag})\n\n"
   ALIVE_MESSAGE += "β―οΈ πΆππΎππΏ β―οΈ : [SUPPORT](https://t.me/Arcane_Bot_Support)\n\n"
   ALIVE_MESSAGE += f"ΰΌ [π³π΄πΏπ»πΎπ](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FArcane120%2Heroku-Setup&template=https%3A%2F%2Fgithub.com%2FArcane120%2FHeroku-Setup) ΰΌ ππΎππ πΎππ½ πΎπΏ βοΈ[{BOT}](https://github.com/Arcane120/ARCANE-USERBOT)  βοΈ\n"   
   await awake.delete() 
   await borg.send_file(arcane.chat_id, ALIVE_PHOTTO,caption=ALIVE_MESSAGE)

CMD_HELP.update(
    {
        "arcane": "Plugin : arcane\
    \n\nSyntax : .awake\
    \nFunction : you can set here costom alive pic .set var ALIVE_PHOTTO (Telegraph link)"
    }
)
