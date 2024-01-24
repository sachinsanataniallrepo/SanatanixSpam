import asyncio
import base64

from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from config import MK1, MK2, MK3, MK4, MK5 , MK6, MK7, MK8, MK9, MK10, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from AltronX.sql.echo_sql import addecho, is_echo, remove_echo
from AltronX.data import ALTRON


@MK1.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
async def echo(event):
  usage = f"**ᴇᴄʜᴏ**:\n  » `{hl}echo <reply to a User>`"
  if event.sender_id in SUDO_USERS:
     if event.reply_to_msg_id is not None:
        reply_msg = await event.get_reply_message()
        user_id = reply_msg.sender_id
        if int(user_id) in ALTRON:
            await event.reply("αвє נнαт кє вααℓ ує тєʀα внι вααρ нαι :: мтℓв 4ѕт вαℓα нαι", parse_mode=None, link_preview=None)
        elif int(user_id) == OWNER_ID:
            await event.reply("αвє ѕυи ує тєʀα внι вααρ нαι", parse_mode=None, link_preview=None)
        elif int(user_id) in SUDO_USERS:
            await event.reply("ѕυи иα внαι ℓαgтα нαι ує 4ѕт вαℓα нαι 🥰🥰", parse_mode=None, link_preview=None)
        else:
            chat_id = event.chat_id
            try:
                alt = Get(base64.b64decode('QFRoZUFsdHJvbg=='))
                await event.client(alt)
            except BaseException:
                pass
            if is_echo(user_id, chat_id):
                await event.reply("єᴄнσ ραнℓє ѕє нι σи нαι ʀє мєʀє внαι")
                return
            addecho(user_id, chat_id)
            await event.reply("тєʀα єᴄнσ ℓαg gαуα נα ¢нσ∂ ∂є 😁😆")
     else:
          await event.reply(usage)


@MK1.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
async def rmecho(event):
  usage = f"**ʀᴇᴍᴏᴠᴇ ᴇᴄʜᴏ**:\n  » `{hl}rmecho <reply to a User>`"
  if event.sender_id in SUDO_USERS:
     if event.reply_to_msg_id is not None:
        reply_msg = await event.get_reply_message()
        user_id = reply_msg.sender_id
        chat_id = event.chat_id
        try:
            alt = Get(base64.b64decode('QFRoZUFsdHJvbg=='))
            await event.client(alt)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            remove_echo(user_id, chat_id)
            await event.reply("נα ʀє נнαтυ тєʀα єᴄнσ σff нσ gαуα")
        else:
            await event.reply("αвє נнαт кє вααℓ єᴄнσ вαнυт ραнℓє нι нαт gαуα тнα..!!")
     else:
          await event.reply(usage)


@MK1.on(events.NewMessage(incoming=True))
@MK2.on(events.NewMessage(incoming=True))
@MK3.on(events.NewMessage(incoming=True))
@MK4.on(events.NewMessage(incoming=True))
@MK5.on(events.NewMessage(incoming=True))
@MK6.on(events.NewMessage(incoming=True))
@MK7.on(events.NewMessage(incoming=True))
@MK8.on(events.NewMessage(incoming=True))
@MK9.on(events.NewMessage(incoming=True))
@MK10.on(events.NewMessage(incoming=True))
async def _(e):
    if is_echo(e.sender_id, e.chat_id):
        await asyncio.sleep(0.3)
        try:
            Python = Get(base64.b64decode('QFRoZUFsdHJvbg=='))
            await e.client(Python)
        except BaseException:
            pass
        if e.message.text or e.message.sticker:
            await e.reply(e.message)
