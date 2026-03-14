import asyncio
import logging
from aiogram import Bot, Dispatcher
from memory.config import BOT_TOKEN
from handlers.command_handlers import *

bot = Bot(token=BOT_TOKEN)

dp = Dispatcher()

async def main():
    dp.include_router(command_handlers)
    await dp.start_polling(bot)
   

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Stopped")