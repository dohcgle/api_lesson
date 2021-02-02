import telebot
token = '1610753174:AAHpqhQf1kdJ1AFOKdZFS14gleR76XwzSHQ'
bot = telebot.TeleBot('1610753174:AAHpqhQf1kdJ1AFOKdZFS14gleR76XwzSHQ')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
         bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')

bot.polling(none_stop=True)