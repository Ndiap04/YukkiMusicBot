import os

import speedtest
import wget
from pyrogram import Client, filters
from pyrogram.types import Message

from Yukki import BOT_ID, SUDOERS, app

__MODULE__ = "Speedtest"
__HELP__ = """

  •  **Perintah** : /speedtest 
  •  **Function** : Periksa Latensi dan Kecepatan Server.

"""


def bytes(size: float) -> str:
    """humanize size"""
    if not size:
        return ""
    power = 1024
    t_n = 0
    power_dict = {0: " ", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        t_n += 1
    return "{:.2f} {}B".format(size, power_dict[t_n])


@app.on_message(filters.command("speedtest") & ~filters.edited & ~filters.user(SUDOERS))
async def statsguwid(_, message):
    m = await message.reply_text("Tes Kecepatan Lari")
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = await m.edit("Menjalankan Unduh SpeedTest")
        test.download()
        m = await m.edit("Menjalankan Tes Kecepatan Unggah")
        test.upload()
        test.results.share()
        result = test.results.dict()
    except Exception as e:
        return await m.edit(e)
    m = await m.edit("Berbagi Hasil Tes Kecepatan")
    path = wget.download(result["share"])

    output = f"""**Hasil Speedtest**
    
<u>**Client:**</u>
**__ISP:__** {result['client']['isp']}
**__Country:__** {result['client']['country']}
  
<u>**Server:**</u>
**__Name:__** {result['server']['name']}
**__Country:__** {result['server']['country']}, {result['server']['cc']}
**__Sponsor:__** {result['server']['sponsor']}
**__Latency:__** {result['server']['latency']}  
**__Ping:__** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, photo=path, caption=output
    )
    os.remove(path)
    await m.delete()
