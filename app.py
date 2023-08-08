import logging

from config import API_TOKEN, ADMINS
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from states import Connection
from keyboards import reply_to_btn

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

@dp.callback_query_handler()
async def send_admin(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer(
        text="Admin xabaringizni kiriting:"
        )
    await Connection.answer_msg.set()
    await state.update_data(user_id=call.data)

@dp.message_handler(state=Connection.answer_msg, content_types=types.ContentTypes.ANY)
async def send_msg_Admin(message: types.Message, state: FSMContext):
    await state.update_data(text=message.text)
    data = await state.get_data()
    try:

        await bot.copy_message(
            chat_id=data.get('user_id'), from_chat_id=message.chat.id, 
            message_id=message.message_id
        )
        await message.reply("✅Xabar yetkazildi!")
    except:
        await message.reply("❌Xabar yetkazilmadi!")
    await state.reset_state(with_data=True)


@dp.message_handler(content_types=types.ContentTypes.ANY)
async def send_msg(message: types.Message):
    msg_id = message.chat.id
    await bot.copy_message(
        chat_id=ADMINS[0], from_chat_id=msg_id, 
        message_id=message.message_id,
        reply_markup=reply_to_btn(msg_id)
        )

if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)