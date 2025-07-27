from telegram import Bot
import asyncio

BOT_TOKEN = "8292608599:AAEdJK3nIph7ToUHFXVdtsYzipeKrCmWnEk"
CHANNEL_ID = -1002621100583  # numeric ID for the channel

async def _send_message_async(message: str):
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHANNEL_ID, text=message)

def notify_telegram_channel(message: str):
    asyncio.run(_send_message_async(message))
