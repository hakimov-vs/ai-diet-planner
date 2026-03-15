from aiogram import Router, types
from aiogram.filters import Command, BaseFilter
from aiogram.fsm.context import FSMContext
from memory.config import ADMINS
from .message_handlers import main_menu

command_handlers = Router()

# USER COMMANDS
@command_handlers.message(Command("start"))
async def start_handler(message: types.Message, state: FSMContext):
    user = message.from_user
    await message.answer(f"Welcome {user.first_name} to the Nutrition Bot! 🍎\n\n"
            "I will help you calculate your daily caloric needs and generate a personalized diet plan.\n\n"
            # "To get started, please provide some basic information about yourself.\n\n"
            # "Click on cancel button at any time to stop our conversation."
            )
    await main_menu(message)

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