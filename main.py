# main.py
import asyncio
import logging
from handlers.admin.panel import router as admin_router
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from handlers.admin.panel import router as admin_router


from config import TOKEN

# Импортируем все роутеры
from handlers.start import router as start_router
from handlers.menu import router as menu_router
from handlers.promotions import router as promotions_router
from handlers.contacts import router as contacts_router
from handlers.feedback import router as feedback_router

logging.basicConfig(level=logging.INFO)

# ← ИСПРАВЛЕНИЕ: теперь так задаётся HTML в aiogram 3.7+
bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

async def main():
    dp.include_router(start_router)
    dp.include_router(menu_router)
    dp.include_router(promotions_router)
    dp.include_router(contacts_router)
    dp.include_router(feedback_router)
    dp.include_router(admin_router)

    print("Бот запущен и готов к работе! 🚀")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())