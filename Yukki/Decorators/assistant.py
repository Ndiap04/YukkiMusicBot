from typing import Dict, List, Union

from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant

from Yukki import (ASSID, ASSMENTION, ASSNAME, ASSUSERNAME, BOT_ID, app,
                   userbot)

from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)

from Yukki.Inline import (sudo_pannel)


def AssistantAdd(mystic):
    async def wrapper(_, message):
        try:
            b = await app.get_chat_member(message.chat.id, ASSID)
            if b.status == "kicked":
                return await message.reply_text(
                    f"⚠️ **Akun Assisten Terkena Banned Dalam Groups!**\n\n» Suruh Admin Untuk Unban @{ASSUSERNAME} || [{ASSID}] Dalam Groups.",
                )
        except UserNotParticipant:
            if message.chat.username:
                try:
                    await userbot.join_chat(message.chat.username)
                except UserAlreadyParticipant:
                    pass
                except Exception as e:
                    await message.reply_text(
                        f"__Asisten Gagal Bergabung__\n\n**Reason**: {e}"
                    )
                    return
            else:
                try:
                    invitelink = await app.export_chat_invite_link(
                        message.chat.id
                    )
                    if invitelink.startswith("https://t.me/+"):
                        invitelink = invitelink.replace(
                            "https://t.me/+", "https://t.me/joinchat/"
                        )
                    await userbot.join_chat(invitelink)
                    await message.reply(
                        f"{ASSMENTION} Berhasil Bergabung!",
                    )
                except UserAlreadyParticipant:
                    pass
                except Exception as e:
                    await message.reply_text(
                        f"__Asisten Gagal Bergabung__\n\n**Reason**: {e}"
                    )
                    return
        return await mystic(_, message)

    return wrapper
