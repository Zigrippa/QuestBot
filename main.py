import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot('5842283991:AAHFRRqJYtub0NyLXIxhftpOcxw1zFpa4dA')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Да')
    btn2 = types.KeyboardButton('Нет')
    markup.row(btn1, btn2)
    bot.send_message(message.chat.id, f'<em>Приветствую тебя, {message.from_user.first_name}!</em>', parse_mode='html',
                     reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Да':
        bot.send_message(message.chat.id, "Хорошо")
    elif message.text == 'Нет':
        bot.send_message(message.chat.id, "Нет, так нет")

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
    btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://google.com')
    btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    markup.row(btn1, btn2)
    bot.reply_to(message, 'Какое красиво фото!', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)




bot.polling(none_stop=True, interval=0)
