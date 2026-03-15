from aiogram.fsm.state import State, StatesGroup

class Register(StatesGroup):
     gender = State()
     age = State()
     weight = State()
     height = State()
     activity = State()
     goal = State()
     bmr = State()
     tdee = State()
     calories = State()