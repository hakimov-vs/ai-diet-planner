from aiogram import Router, types
from aiogram.filters import Command, BaseFilter
from memory.config import ADMINS

command_handlers = Router()

# USER COMMANDS
@command_handlers.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("start")

@command_handlers.message(Command("help"))
async def help_handler(message: types.Message):
    await message.answer("help")

@command_handlers.message(Command("cancel"))
async def cancel_handler(message: types.Message):
    await message.answer("cancel")


# ADMIN COMMANDS
class IsAdmin(BaseFilter):
    async def __call__(self, message: types.Message):
        if message.from_user.id in ADMINS:
            return True
        else:
            await message.reply("You are not admin!!!")


@command_handlers.message(Command("getusers"), IsAdmin())
async def getusers(message: types.Message):
    await message.answer("Here is all users")