import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from fetch_weather import fetch_weather
from parse_data import parse_data
from datetime import datetime
from config import config
import markups as nav
from localizations import translate
from cat_api import fetch_cat_image
from random import choice

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.bot_token.get_secret_value())
# Диспетчер
dp = Dispatcher()
dp["started_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
dp["name"] = 'Kelltic'
dp["language"] = 'en'

phrases = ["You asked for it))", "This one is my favorite xD", "Omg its so pretty!", "Well, it is what it is", "I always wanted this breed btw", "Those eyes will haunt me in the nigth!", "Looks like you!", "I hope you have a better day!", "Why they're so prettyyy", "I love cats so much...", "I wanna cry cause of this cuties...", "I wanna be a cat myself, not the robot..."]


# Хэндлер на команду /start
# @dp.message(Command("start"))
# async def cmd_start(message: types.Message, name):
#     await message.answer(f"Hello! Please, choose your language", reply_markup=nav.lang_menu)
#     dp['language'] = 'ru'
#     print(dp['language'])


@dp.message(Command(commands=['start']))
async def cmd_start(message: types.Message, name):
    await message.answer(f'''Hey! Currently I only have 2 available commands you can use: 

1) /weather
- You can use it by simply writing me message in the following pattern: 
                         
    /weather <City_Name_Like_This>
                         
    Examples: 
        /weather Moscow
        /weather Stary_Oskol
        /weather Kyiv)
                         
2) /cat
                         
    - I will send you a random cat image ^_^      ''')


@dp.message(Command("worktime"))
async def cmd_worktime(message: types.Message, started_at):
    await message.answer(f"Been working since: {started_at}")

@dp.message(Command("cat"))
async def cmd_cat(message: types.Message, started_at):
    result = await fetch_cat_image()  
    text = choice(phrases)
    await message.answer(text=text)
    await bot.send_photo(photo=result[0]['url'], chat_id=message.from_user.id)


@dp.message(Command("weather"))
async def cmd_weather(
        message: types.Message,
        command: Command
):
    # Если не переданы никакие аргументы, то
    # command.args будет None
    if command.args is None:
        await message.answer(
            "Error: No city specified. Try to use this format: /weather <City>"
        )
        return
    # Пробуем разделить аргументы на две части по первому встречному пробелу

    try:
        parts = command.args.split(' ')
        if len(parts) > 1:
            other_data = ' '.join(parts[1:])
            print(f"Other data: {other_data}")
        else:
            other_data = ''
        city = parts[0]
        if '_' in city:
            city_formatted = city.replace('_', ' ')
        else:
            city_formatted = city
        

        data = await fetch_weather(city_formatted)

        # print(f"Data: {data}")

        if data['cod'] == 200:

            #! Вот тут будет перевод, прям внутри parse_data function
            result = await parse_data(data, language=dp['language'])

            if other_data:
                await message.answer(f'''{result}\n
    Unknown data: {other_data}''')
            else:
                await message.answer(result)
        else:
            await message.answer(
            "Error: Invalid city name. \nExamples: Moscow, Stary_Oskol, Belgorod, Voronezh..."
            
        )
    # Если получилось меньше двух частей, вылетит ValueError
    except ValueError:
        await message.answer(
            "Error: wrong command format. Example:\n"
            "/weather <City>"
        )
        return

@dp.callback_query()
async def set_language(callback: types.CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    lang = callback.data[5:]
    text = translate("Succesfully! Using English now", language=lang)
    await bot.send_message(text=text, chat_id=callback.from_user.id)

@dp.message()
async def send_echo(message: types.Message):
    await message.answer(text=f'Unfortunetely, at the moment I am not smart enough to answer that... Try to write /start')

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())