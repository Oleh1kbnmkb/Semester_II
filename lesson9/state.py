from aiogram.dispatcher.filters.state import State, StatesGroup


class RegistrationStates(StatesGroup):
    step1 = State()
    step2 = State()
    step3 = State()