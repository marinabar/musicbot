import pandas as pd
import telebot
import os

token = "5048192501:AAFFzzqB-_VD9UZWhJ5Ip7QPAgRds1S3XVw"
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
    folder = '/home/marina/Documents/spotscrape/coll'
    songs = os.listdir(folder)
    for element in songs:
        name = os.path.join(folder, element)
        bot.send_audio(user_id, audio=open(name, 'rb'))

bot.polling(none_stop=True)