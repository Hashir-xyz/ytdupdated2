from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Currently Only supports Youtube Single  (No playlist) Just Send Youtube Url,If Failed To Download Just Send Link To Customer Care"
    await message.reply_text(helptxt)
