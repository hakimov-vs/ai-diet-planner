from aiogram import Router, F, types
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from memory.states import Register
from .message_handlers import main_menu

state_handlers = Router()

@state_handlers.message(StateFilter("*"), F.text.casefold() == "cancel")
async def cancel_state(message: types.Message, state: FSMContext):
    await state.clear()
    await main_menu(message)


@state_handlers.message(StateFilter(Register.age))
async def get_age(message: types.Message, state: FSMContext):
    age = message.text
    if age.isdigit():
        age = int(age)
        if age > 1 and age < 120:
            await message.answer("Ready to go further")
        else:
            await message.answer("Please enter a valid age between 1 and 120:")
    else:
        await message.answer("Please enter a valid number for your age:")