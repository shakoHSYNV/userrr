import asyncio
from collections import deque

from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot import CMD_HELP


@bot.on(admin_cmd(pattern="think$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "think")
    deq = deque(list("๐ค๐ง๐ค๐ง๐ค๐ง"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern=r"lmao$"))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "lmao")
    deq = deque(list("๐๐คฃ๐๐คฃ๐๐คฃ"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern=r"nothappy$"))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "nathappy")
    deq = deque(list("๐โน๏ธ๐โน๏ธ๐โน๏ธ๐"))
    for _ in range(48):
        await asyncio.sleep(0.4)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(outgoing=True, pattern="clock$"))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "clock")
    deq = deque(list("๐๐๐๐๐๐๐๐๐๐๐"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern=r"muah$"))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "muah")
    deq = deque(list("๐๐๐๐๐"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern="heart$"))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "heart")
    deq = deque(list("โค๏ธ๐งก๐๐๐๐๐ค"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern="gym$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "gym")
    deq = deque(list("๐โ๐โ๐คธโ๐โ๐โ๐คธโ๐โ๐โ๐คธโ"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern=f"earth$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "earth")
    deq = deque(list("๐๐๐๐๐๐๐๐"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(outgoing=True, pattern="moon$"))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "moon")
    deq = deque(list("๐๐๐๐๐๐๐๐"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern=f"smoon$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "smoon")
    animation_interval = 0.1
    animation_ttl = range(101)
    await event.edit("smoon..")
    animation_chars = [
        "๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐",
        "๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐",
        "๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐",
        "๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐",
        "๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐",
        "๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐",
        "๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐",
        "๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8])


@bot.on(admin_cmd(pattern=f"tmoon$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "tmoon")
    animation_interval = 0.1
    animation_ttl = range(117)
    await event.edit("tmoon")
    animation_chars = [
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 32])

@bot.on(admin_cmd(pattern=f"hart$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(20)
    event = await edit_or_reply(event, "โค๏ธ")
    animation_chars = ["๐ค", "โค๏ธ", "๐ค", "โค๏ธ", "โ"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 4])


@bot.on(admin_cmd(pattern=f"anim$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(20)
    event = await edit_or_reply(event, "๐ข")
    animation_chars = [
        "๐",
        "๐ง",
        "๐ก",
        "๐ข",
        "๐",
        "๐ง",
        "๐ก",
        "๐ข",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 10])


@bot.on(admin_cmd(pattern=f"fnl$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(6)
    event = await edit_or_reply(event, "Hey There....")
    animation_chars = ["๐๐ฟ", "๐๐พ", "๐๐ฝ", "๐๐ผ", "โ๐"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 6])


@bot.on(admin_cmd(pattern=f"monkey$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(12)
    event = await edit_or_reply(event, "Hey There....")
    animation_chars = ["๐ต", "๐", "๐", "๐", "๐โ๐ต๐"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 6])

@bot.on(admin_cmd(pattern=f"hand$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(13)
    event = await edit_or_reply(event, "๐๏ธ")
    animation_chars = [
        "๐",
        "๐",
        "โ๏ธ",
        "๐",
        "๐",
        "๐",
        "โ๏ธ",
        "๐ค",
        "๐",
        "๐ค",
        "๐ค",
        "๐๏ธ",
        "๐",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 13])


@bot.on(admin_cmd(pattern=f"gsg$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(12)
    event = await edit_or_reply(event, "ContDown....")
    animation_chars = [
        "๐",
        "9๏ธโฃ",
        "8๏ธโฃ",
        "7๏ธโฃ",
        "6๏ธโฃ",
        "5๏ธโฃ",
        "4๏ธโฃ",
        "3๏ธโฃ",
        "2๏ธโฃ",
        "1๏ธโฃ",
        "0๏ธโฃ",
        "๐",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 12])


@bot.on(admin_cmd(pattern=r"theart$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(54)
    event = await edit_or_reply(event, "๐ค")
    animation_chars = [
        "โค๏ธ",
        "๐งก",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐ค",
        "๐",
        "๐",
        "โค๏ธ",
        "๐งก",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐ค",
        "๐",
        "๐",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])



CMD_HELP.update(
    {
        "animoji": """**Plugin : **`animoji`
        
**Commands in animoji are **
  โข  `.think`
  โข  `.lmao`
  โข  `.nothappy`
  โข  `.clock`
  โข  `.muah`
  โข  `.heart`
  โข  `.gym`
  โข  `.earth`
  โข  `.moon`
  โข  `.smoon`
  โข  `.tmoon`
  โข  `.hart`
  โข  `.anim`
  โข  `.fnl`
  โข  `.monkey`
  โข  `.hand`
  โข  `.gsg`
  โข  `.theart`
  
**Function : **__Different kinds of emoji animation commands check yourself for their animation .__"""
    }
)
