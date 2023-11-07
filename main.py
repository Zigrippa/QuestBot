import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot('5842283991:AAHFRRqJYtub0NyLXIxhftpOcxw1zFpa4dA')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'<em>Приветствую тебя, {message.from_user.first_name}!</em>', parse_mode='html')

@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, 'Список доступных комманд:\n'
                                      '/start\n'
                                      '/help\n')

#@bot.message_handler(commands=['site', 'website'])
#def start(message):
#    webbrowser.open('https://google.com')

@bot.message_handler()
def info(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, "Привет, чем я могу тебе помочь?")
    elif message.text.lower() == "id":
        bot.reply_to(message, f'ID:{message.from_user.id}')

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на сайт', url='https://google.com'))
    markup.add(types.InlineKeyboardButton('Удалить фото', callback_data='delete'))
    bot.reply_to(message, 'Какое красиво фото!', reply_markup=markup)


bot.polling(none_stop=True, interval=0)
