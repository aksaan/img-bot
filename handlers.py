from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command


router = Router()

@router.message(Command('start'))
async def start_handler(msg : Message):
    await msg.answer('Напиши мне что угодно и я пришлю Id')
    
@router.message()
async def msg_handler(msg : Message):
    await msg.answer(f'Твой Id : {msg.from_user.id}')