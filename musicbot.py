import pandas as pd
import telebot
import os

folder = str(input("specify the desired folder"))
token = str(input("Please paste your token"))
bot = telebot.TeleBot(token=token)
@bot.message_handler(commands=['start'])
def start(message):
    text = message.text
    user_id = message.chat.id
    bot.send_message(user_id, "Hello")


@bot.message_handler(commands=['all'])
def all(message):
    text = message.text
    user_id = message.chat.id
    songs = os.listdir(folder)
    for element in songs:
        name = os.path.join(folder, element)
        bot.send_audio(user_id, audio=open(name, 'rb'))

bot.polling(none_stop=True)
