from aiogram import Router, types, F
from memory.states import Register
from aiogram.fsm.context import FSMContext

message_handlers = Router()

async def main_menu(message: types.Message):
    user_here = False
    if user_here:
        main_menu_kb = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text="Generate menu again")], [types.KeyboardButton(text="Update my info")]], resize_keyboard=True)
    else:
        main_menu_kb = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text="Get Started")]], resize_keyboard=True)
    await message.answer("Choose from menu", reply_markup=main_menu_kb)


@message_handlers.message(F.text.casefold() == "get started")
async def register_age(message: types.Message, state: FSMContext):
     await state.set_state(Register.age)
     menu_kb = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text="Cancel")]], resize_keyboard=True)
     
     await message.answer("To get started, please provide some basic information about yourself.\n\nClick on cancel button at any time to stop our conversation.")
     await message.answer("Now please enter your age:", reply_markup=menu_kb)

@message_handlers.message()
async def message_handler(message: types.Message):
    await main_menu(message)