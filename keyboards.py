from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def reply_to_btn(message_id):
    reply_btn = InlineKeyboardMarkup()
    button = InlineKeyboardButton(text='🖋Reply to Message', callback_data=message_id)
    reply_btn.add(button)
    return reply_btn