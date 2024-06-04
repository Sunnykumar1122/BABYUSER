import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Rolex"])

async def join(client):
    try:
        await client.join_chat("babe_bot_update")
    except BaseException:
        pass
