import asyncio
from aiogram.types import FSInputFile
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

text_1=""
text_2=""

kb_start = [
        [types.KeyboardButton(text="Информация"),types.KeyboardButton(text="Обменники")],
        [types.KeyboardButton(text="Личный кабинет"),types.KeyboardButton(text="Избранные обменники")],
    ]
keyboard_start = types.ReplyKeyboardMarkup(
    keyboard=kb_start,
    resize_keyboard=True,
    input_field_placeholder="Выберите действие"
)
start_image = FSInputFile("start.png")
task_image=FSInputFile("task.png")
bot = Bot(token='', parse_mode="HTML") #insert token

dp = Dispatcher()


@dp.message(Command("start"))
async def process_start_command(message: types.Message):
    await message.answer_photo(start_image, caption=text_1, reply_markup=keyboard_start)

@dp.message(lambda message: message.text == "Обменники")
async def exchangers_list(message: types.Message):
    await message.answer("A BTC - 100$\nB BTC - 200$\nC BTC - 300$", reply_markup=keyboard_start)


@dp.message(Command("f91bd0e12c58dd1567ed27ca01fdedd5"))
async def process_start_command(message: types.Message):
    await message.reply("Пароль принят")


@dp.message(lambda message: message.text == "Информация")
async def exchangers_list(message: types.Message):
    await message.answer_photo(task_image,caption=text_2, reply_markup=keyboard_start)



async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
