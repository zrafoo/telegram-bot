import asyncio
from aiogram.types import FSInputFile
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

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
    await message.answer_photo(start_image, caption='''
                            Мониторинг обменников <strong>BestChange</strong>
                            
Добро пожаловать на телеграм бота мониторинга обменников <strong>BestChange</strong>! 
Наш мониторинг обменных пунктов разработан для тех, кто хочет безопасно обменивать электронные деньги в сети интернет с незначительными комиссионными затратами.
                                                    ''', reply_markup=keyboard_start)

@dp.message(lambda message: message.text == "Обменники")
async def exchangers_list(message: types.Message):
    await message.answer("A BTC - 100$\nB BTC - 200$\nC BTC - 300$", reply_markup=keyboard_start)


@dp.message(Command("f91bd0e12c58dd1567ed27ca01fdedd5"))
async def process_start_command(message: types.Message):
    await message.reply("Пароль принят")


@dp.message(lambda message: message.text == "Информация")
async def exchangers_list(message: types.Message):
    await message.answer_photo(task_image,caption='''
    <strong>Подробнее о мониторинге обменников</strong>

В интернете существует множество обменных пунктов электронных валют, и каждый обменник устанавливает свои курсы, постоянно их корректируя. При этом даже самые авторитетные и крупные обменные пункты не всегда могут иметь в наличии необходимую вам сумму. Как же найти самый оптимальный обменник, где можно беспрепятственно обменять деньги с минимальными потерями? Использование сервиса по мониторингу обменных пунктов поможет вам сэкономить время и деньги. Поиск курсов ведется по нескольким десяткам проверенных и надежных автоматических электронных обменников.
    ''', reply_markup=keyboard_start)



async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
