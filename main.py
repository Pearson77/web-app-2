from telebot import TeleBot
from telebot.types import Message

from keyboard import keyboard
from config import token

bot = TeleBot(token=token)


@bot.message_handler(commands=['start', 'site'])
def send_sites_choice(message: Message):
    bot.send_message(
        chat_id=message.chat.id,
        text="Что хотите открыть в режиме WebAPP?",
        reply_markup=keyboard
    )


if __name__ == "__main__":
    bot.infinity_polling(skip_pending=True)
