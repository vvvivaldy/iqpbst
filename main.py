import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

# Инициализация бота и диспетчера
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

# ID чата для пересылки сообщений
SUPPORT_CHAT_ID = int(os.getenv("SUPPORT_CHAT_ID"))


@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот технической поддержки. Напишите ваше сообщение, и я перешлю его в поддержку.")


@dp.message(Command("answer"))
async def handle_support_reply(message: types.Message):
    # Проверяем, является ли сообщение ответом на пересланное сообщение
    txt = message.text
    if txt.find('/answer') or txt.find('/ответ'):
        try:
            # Получаем ID пользователя, которому нужно отправить ответ
            user_id = ''
            for x in txt.split(' ')[1]:
                if x in '1234567890':
                    user_id += x
                else:
                    break
            
            # Отправляем ответ пользователю
            await bot.send_message(user_id, f"Ответ от поддержки:\n{message.text.replace(f'/answer {user_id}', '')}")
        except:
            pass


@dp.message(Command("ответ"))
async def handle_support_reply2(message: types.Message):
    # Проверяем, является ли сообщение ответом на пересланное сообщение
    txt = message.text
    if txt.find('/answer') or txt.find('/ответ'):
        try:
            # Получаем ID пользователя, которому нужно отправить ответ
            user_id = ''
            for x in txt.split(' ')[1]:
                if x in '1234567890':
                    user_id += x
                else:
                    break
            
            # Отправляем ответ пользователю
            await bot.send_message(user_id, f"Ответ от поддержки:\n{message.text.replace(f'/answer {user_id}', '')}")
        except:
            pass



@dp.message()
async def forward_to_support(message: types.Message):
    # Пересылаем сообщение в чат поддержки
    if message.chat.id != SUPPORT_CHAT_ID:
        forwarded_message = await bot.send_message(
            SUPPORT_CHAT_ID,
            f"Сообщение от пользователя\nID: {message.from_user.id}\nusername: {message.from_user.username}\nИмя: {message.from_user.full_name}"
        )

        await bot.forward_message(chat_id=SUPPORT_CHAT_ID, from_chat_id=message.from_user.id, message_id=message.message_id)
    

async def main():
    print('starting...')
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())