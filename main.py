import asyncio
from aiogram import Bot, Dispatcher, types, Router
from memory.config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)

dp = Dispatcher()

message = Router()


@message.message()
async def echo(message: types.Message):
    await message.answer(message.text)


async def main():
    dp.include_router(message)
    await dp.start_polling(bot)
   

if __name__ == "__main__":
    asyncio.run(main())