#! /usr/bin/env python
# -*- coding: utf-8 -*-
from config import interval, phrases_list, hello_list, who_is_bot, i_am_list, yes_answers
import telebot, random
import tok
import requests
import time

bot = telebot.TeleBot(tok.tok)

message_count = {}


@bot.message_handler(commands=["conf"])
def handle_config_info(message):
    C = 'Думаю что сказать где-то {} сообщений'.format(interval)
    bot.send_message(message.chat.id, C)
    try:
        CC = 'Осталось {}'.format(interval-count[message.chat.id])
        bot.send_message(message.chat.id, CC)
    except KeyError:
        pass


@bot.message_handler(regexp=r'([пП]ривет)|([зЗ]дарова?)|([дД]оброе\sутро)|([дД]обрый\sдень)')
def hello_to_all(message):
    bot.send_message(message.chat.id, random.choice(hello_list))

@bot.message_handler(regexp=r'да,?\s[Мм]а[ий]ор')
def acception(message):
    bot.send_message(message.chat.id, random.choice(yes_answers))

@bot.message_handler(regexp=r'[мМ]айор\??')
def say_i_am(message):
    bot.send_message(message.chat.id, random.choice(i_am_list))


@bot.message_handler(regexp=r'(\sбот\s)|(^[бБ]от\?$)|(\s[бБ]от\?)|(^[бБ]от$)')
def say_not_bot(message):
    bot.send_message(message.chat.id, random.choice(who_is_bot))


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    global message_count
    if len(message.text) > 0:
        try:
            message_count[message.chat.id] +=1
        except KeyError:
            message_count[message.chat.id] = 0
            message_count[message.chat.id] += 1
        if message_count[message.chat.id] > interval:
            bot.send_message(message.chat.id, random.choice(phrases_list))
            message_count[message.chat.id] = 0



if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
            time.sleep(10)
        except requests.exceptions.ConnectionError as e:
            print(str(e))
            print("sleep 25sec")
            time.sleep(25)
        except requests.exceptions.ReadTimeout as t:
            print(str(t))
            print("sleep 30sec")
            time.sleep(30)
