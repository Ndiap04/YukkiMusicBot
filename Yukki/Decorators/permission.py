from typing import Dict, List, Union

from Yukki import BOT_ID, app


def PermissionCheck(mystic):
    async def wrapper(_, message):
        a = await app.get_chat_member(message.chat.id, BOT_ID)
        if a.status != "administrator":
            return await message.reply_text(
                "💡 **Saya Perlu Menjadi Admin!**:\n"
                + "\n» Jadikan Saya Admin Agar Saya Dapat Memutar Music Diobrolan Anda."
            )
        if not a.can_manage_voice_chats:
            await message.reply_text(
                "🚧 **Saya Tidak Memiliki izin Yang Diperlukan Untuk Melakukan Tindakan ini!**"
                + "\n» Silahkan Ganti Izin Saya Menjadi (Kelola Obrolan Video)"
            )
            return
        if not a.can_delete_messages:
            await message.reply_text(
                "🚧 **Saya Tidak Memiliki izin Yang Diperlukan Untuk Melakukan Tindakan ini!**"
                + "\n» Silahkan Ganti Izin Saya Menjadi (Hapus Pesan)"
            )
            return
        if not a.can_invite_users:
            await message.reply_text(
                "🚧 **Saya Tidak Memiliki izin Yang Diperlukan Untuk Melakukan Tindakan ini!**"
                + "\n» Silahkan Ganti Izin Saya Menjadi (Undang Pengguna Dengan Tautan)"
            )
            return
        return await mystic(_, message)

    return wrapper
