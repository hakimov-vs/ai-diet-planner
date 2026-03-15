import asyncio
import logging
from aiogram import Bot, Dispatcher
from memory.config import BOT_TOKEN
from handlers.command_handlers import command_handlers
from handlers.state_handlers import state_handlers
from handlers.message_handlers import message_handlers

bot = Bot(token=BOT_TOKEN)

dp = Dispatcher()

async def main():
    dp.include_router(command_handlers)
    dp.include_router(state_handlers)
    dp.include_router(message_handlers)
    await dp.start_polling(bot)
   

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Stopped")