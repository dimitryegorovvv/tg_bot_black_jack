import telebot
from token_file import token
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,f'здравствуйте, {message.from_user.first_name}')

@bot.message_handler()
def main(message):
    if message.text.lower()=='привет':
        bot.send_message(message.chat.id, 'привет')


bot.polling(none_stop=True)