#! /usr/bin/env python
# -*- coding: utf-8 -*-
import telebot, random
import tok
import requests
import time
import re

from config import interval, phrases_list, hello_list, who_is_bot, yes_answers, i_am_list
from weather import forecast_weather_req

bot = telebot.TeleBot(tok.tok)

message_count = {}

def flatten(tup):
	result = []
	for el in tup:
		if hasattr(el, "__iter__") and type(el) != str:
			result.extend(flatten(el))
		else:
			result.append(el)
	return result

@bot.message_handler(commands=["conf"])
def handle_config_info(message):
    C = 'Думаю что сказать где-то {} сообщений'.format(interval)
    bot.send_message(message.chat.id, C)
    try:
        CC = 'Осталось {}'.format(interval-message_count[message.chat.id])
        bot.send_message(message.chat.id, CC)
    except KeyError:
        pass


@bot.message_handler(regexp=r'([пП]ривет)|([зЗ]дарова?)|([дД]оброе\sутро)|([дД]обрый\sдень)')
def hello_to_all(message):
	bot.send_message(message.chat.id, random.choice(hello_list))

@bot.message_handler(regexp=r'да,?\s[Мм]а[ий]ор')
def acception(message):
	bot.send_message(message.chat.id, random.choice(yes_answers))


@bot.message_handler(regexp=r'^[мМ]айор\??$')
def i_am_here(message):
	bot.send_message(message.chat.id, random.choice(i_am_list))

@bot.message_handler(regexp=r'^[мМ]айор,?')
def added_func_parsing(message):
	pog_trig = re.search(r'[пП][оО][гГ][оО][дД]', message.text).group().lower()
	if pog_trig == 'погод':
		arg_words = message.text[6:].split()
		try:
			city = re.search(r'\sво?\s(?P<city>\w+)\??', message.text).group('city')
			if 'завтра' in arg_words:
				when_day = 'tomorrow'
			elif 'послезавтра' in arg_words:
				when_day = 'after_tomorrow'
			else:
				when_day = None
			if 'утро' in arg_words or 'утра' in arg_words or 'утром' in arg_words:
				when_time = 'morn'
			elif 'день' in arg_words or 'днем' in arg_words:
				when_time = 'day'
			elif 'вечер' in arg_words or 'вечера' in arg_words:
				when_time = 'evn'
			elif 'ночь' in arg_words or 'ночью' in arg_words or 'ноч' in arg_words:
				when_time = 'night'
			else:
				when_time = None
			#res = ' '.join((when_time or ' ', when_day or ' ', city or ' '))
			res = flatten(forecast_weather_req(city, when_day, when_time))
			go_text = 'В {} будет примерно {}\xB0С, {}. Инфа от станции "{}"'.format(city, res[1], res[2], res[0])
			bot.send_message(message.chat.id, go_text)
		except AttributeError:
			bot.send_message(message.chat.id, 'Ты не сказал где')


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
			time.sleep(3)
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
