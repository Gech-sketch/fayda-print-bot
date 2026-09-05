import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

API_TOKEN = '8926611323:AAE1vn6ZC8MfcFRtueQaMw46pGd6GV0v1jU'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    welcome_text = (
        "እንኳን ደህና መጡ! 🇪🇹\n\n"
        "ይህ ቦት የፋይዳ (Fayda) መረጃዎን ወደ ፕሪንት ሊደረግ የሚችል ፎርማት ይቀይራል።\n"
        "ለመጀመር እባክዎ የፋይዳ ቁጥርዎን (FAN) ይላኩ።"
    )
    await message.answer(welcome_text)

@dp.message()
async def handle_user_input(message: types.Message):
    user_text = message.text.strip()
    
    if user_text.startswith("FT") or "ethiotelecom.et" in user_text:
        await message.answer("የክፍያ ማረጋገጫዎ ደርሷል! እያጣራን ነው...")
    else:
        await message.answer(
            f"የተላከው የፋይዳ ቁጥር: <b>{user_text}</b> ተቀብለናል።\n"
            "ሰነዱን ወደ ፕሪንት ፎርማት ለመቀየር እባክዎ 15 ብር ይክፈሉ።", 
            parse_mode="HTML"
        )

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
  
