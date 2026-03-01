from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import webbrowser

bot = Bot('8473742081:AAGiUeuS7LlT4CIn78blpw5fZyj998g8Mo8')
dp = Dispatcher()
# Код бота
@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer('Привет!')

@dp.message(Command('help'))
async def help(message: types.Message):
    await message.reply('/start\n/help')

@dp.message(Command('faq'))
async def faq(message: types.Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Мой FunPay', url='https://funpay.com/users/9860902/')]
    ])
    await message.answer('Бот создан 20.02.2026 для обучения', reply_markup=markup)

@dp.message(Command('myinfo'))
async def myinfo(message: types.Message):
    user = message.from_user
    await message.reply(f'Твой айди: {user.id}\nТвой язык: {user.language_code}\nТвой юзернейм: {user.username}')

@dp.message(Command('YouTube'))
async def youtube(message: types.Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='YouTube', url='https://youtube.com/')]
    ])
    await message.answer('Посмотри ютубчик', reply_markup=markup)

# Запуск
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())