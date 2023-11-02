import openai
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot_token = "5993557369:AAE6Hbdh72lV7y5swOvS_T2Hlu0HFSszTQQ"
openai.api_key = "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"

bot = Bot(token=bot_token)
dp = Dispatcher(bot)


@dp.message_handler()
async def send(message: types.Message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.5,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        stop=["You:"],
    )
    await message.answer(response.choices[0].text)


executor.start_polling(dp, skip_updates=True)
