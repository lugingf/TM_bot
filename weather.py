# -*- coding: utf-8 -*-


import requests
import time
from datetime import datetime, timedelta
from tok import weather_key

base_url = 'http://api.openweathermap.org/data/2.5/weather'  # запрос для текущей погоды
forecast_url = 'http://api.openweathermap.org/data/2.5/forecast'  # прогноз на 5 дней с интервалом в 3 часа


def forecast_weather_format(forecast_data_list, when_day=None, when_time=None):
	curr_time = datetime.today()
	tomorrow_day = (curr_time + timedelta(days=1)).day
	after_tomorrow_day = (curr_time + timedelta(days=2)).day
	for i in range(len(forecast_data_list) - 1):
		weather_dt = datetime.fromtimestamp(forecast_data_list[i]['dt'])
		if when_day == "tomorrow" and when_time == "morn":  # TODO: 1) изменить структуру условий, объединив when_day и weather_dt; 2) слишком много одинакового кода
			if weather_dt.day == tomorrow_day and weather_dt.hour == 9:
				temp_forecast = int(forecast_data_list[i]['main']['temp'])
				weather_desc_forecast = forecast_data_list[i]['weather'][0]['description']
				#return (str(weather_dt), temp_forecast, weather_desc_forecast)
				return (temp_forecast, weather_desc_forecast)
		elif when_day == "tomorrow" and when_time == "day":
			if weather_dt.day == tomorrow_day and weather_dt.hour == 15:
				temp_forecast = int(forecast_data_list[i]['main']['temp'])
				weather_desc_forecast = forecast_data_list[i]['weather'][0]['description']
				return (temp_forecast, weather_desc_forecast)
		elif when_day == "tomorrow" and when_time == "evn":
			if weather_dt.day == tomorrow_day and weather_dt.hour == 21:
				temp_forecast = int(forecast_data_list[i]['main']['temp'])
				weather_desc_forecast = forecast_data_list[i]['weather'][0]['description']
				return (temp_forecast, weather_desc_forecast)
		elif when_day == "tomorrow" and when_time == "night":
			if weather_dt.day == tomorrow_day and weather_dt.hour == 3:
				temp_forecast = int(forecast_data_list[i]['main']['temp'])
				weather_desc_forecast = forecast_data_list[i]['weather'][0]['description']
				return (temp_forecast, weather_desc_forecast)
		elif when_day == "after_tomorrow" and when_time == "morn":
			if weather_dt.day == after_tomorrow_day and weather_dt.hour == 9:
				temp_forecast = int(forecast_data_list[i]['main']['temp'])
				weather_desc_forecast = forecast_data_list[i]['weather'][0]['description']
				return (temp_forecast, weather_desc_forecast)
		elif when_day == "after_tomorrow" and when_time == "day":
			if weather_dt.day == after_tomorrow_day and weather_dt.hour == 15:
				temp_forecast = int(forecast_data_list[i]['main']['temp'])
				weather_desc_forecast = forecast_data_list[i]['weather'][0]['description']
				return (temp_forecast, weather_desc_forecast)
		elif when_day == "after_tomorrow" and when_time == "evn":
			if weather_dt.day == after_tomorrow_day and weather_dt.hour == 21:
				temp_forecast = int(forecast_data_list[i]['main']['temp'])
				weather_desc_forecast = forecast_data_list[i]['weather'][0]['description']
				return (temp_forecast, weather_desc_forecast)
		elif when_day == "after_tomorrow" and when_time == "night":
			if weather_dt.day == after_tomorrow_day and weather_dt.hour == 3:
				temp_forecast = int(forecast_data_list[i]['main']['temp'])
				weather_desc_forecast = forecast_data_list[i]['weather'][0]['description']
				return (temp_forecast, weather_desc_forecast)
		elif when_day == "tomorrow" and when_time == None:
			if weather_dt.day == tomorrow_day and weather_dt.hour == 15:
				temp_forecast = int(forecast_data_list[i]['main']['temp'])
				weather_desc_forecast = forecast_data_list[i]['weather'][0]['description']
				return (temp_forecast, weather_desc_forecast)
		elif when_day == "after_tomorrow" and when_time == None:
			if weather_dt.day == after_tomorrow_day and weather_dt.hour == 15:
				temp_forecast = int(forecast_data_list[i]['main']['temp'])
				weather_desc_forecast = forecast_data_list[i]['weather'][0]['description']
				return (temp_forecast, weather_desc_forecast)


def forecast_weather_req(city, when_day=None, when_time=None):
	parameters = {'APPID': weather_key,
				  'units': 'metric',
				  'lang': 'ru'}
	if city == None:
		return 402
	else:
		parameters.update({'q': city})
		if when_day == when_time == None:
			current_weather = requests.get(base_url, parameters)
			if current_weather.status_code in (500, 502):
				return 402
			else:
				temp_now = int(current_weather.json()['main']['temp'])
				loc_now = current_weather.json()['name']
				weather_desc_now = current_weather.json()['weather'][0]['description']
				return (loc_now, temp_now, weather_desc_now)
		else:
			forecast_weather = requests.get(forecast_url, parameters)
			if forecast_weather.status_code == 500:
				return 402
			else:
				return (forecast_weather.json()['city']['name'],
						forecast_weather_format(forecast_weather.json()['list'], when_day or None,
												when_time or None))  # forecast_data = forecast.json()['list']  список, данные по погоде на 5 дней



if __name__ == '__main__':
	#print(forecast_weather_req(None))
	print(forecast_weather_req('ggggggg'))
	#print(forecast_weather_req('Moscow', 'tomorrow'))
	#print(forecast_weather_req('Moscow', 'after_tomorrow'))
	# print(forecast_weather_req('Moscow', 'after_tomorrow', 'morn'))
	# print(forecast_weather_req('Moscow', 'after_tomorrow', 'day'))
	print(forecast_weather_req('пппппппп', 'tomorrow', 'night'))
	# print(forecast_weather_req('Владивосток', 'tomorrow', 'day'))
	# print(forecast_weather_req('Владивосток', 'tomorrow', 'evn'))
	# print(forecast_weather_req('Rostov'))


 # \xB0С - символ градуса