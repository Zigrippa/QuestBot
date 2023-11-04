import telebot

bot = telebot.TeleBot('5842283991:AAHFRRqJYtub0NyLXIxhftpOcxw1zFpa4dA')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/task":
        pass
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Приветствую тебя!')


bot.polling(none_stop=True, interval=0)
