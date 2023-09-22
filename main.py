import os
import asyncio 
import dotenv

from aiogram import Bot, Dispatcher 
from aiogram.enums.parse_mode import ParseMode 
from aiogram.fsm.storage.memory import MemoryStorage 

from handlers import router


dotenv.load_dotenv()

async def main():
    bot = Bot(token=os.environ.get('TOKEN'), parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage()) 
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__' : 
    asyncio.run(main())