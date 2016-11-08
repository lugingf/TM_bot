#-*- coding: utf-8 -*-

'''
 payload = {'key1': 'value1', 'key2': 'value2'}
 r = requests.get('http://httpbin.org/get', params=payload)
 r.json()
 print(r.url)
http://httpbin.org/get?key1=value1&key2=value2&key2=value3

'Конвертировать время POSIX в datetime'
print datetime.fromtimestamp(time.time())
#> 2010-08-14 02:58:15.057613

'Сдвинуть время'
print d + timedelta(days=1, hours=1)
#> 2010-08-15 03:58:15.057538

'Получить день недели, 0 - Пн, 6 - Вс'
print d.weekday()
#> 5

скажи погоду дата/время
какая погода дата/время
что там по поводу погоды дата/время
что там по погоде дата/время
погода дата/время
по датам: сегодня/завтра/послезавтра
а время: ночь/утро/день/вечер

result_examples:
current_weather.json()
{'coord': {'lon': 37.62, 'lat': 55.75}, 'base': 'stations', 'sys': {'type': 1, 'country': 'RU', 'message': 0.0051, 'sunset': 1478612009, 'sunrise': 1478580743, 'id': 7323}, 'wind': {'deg': 240, 'speed': 4}, 'main': {'pressure': 1012, 'temp_max': 2, 'temp_min': 0, 'humidity': 94, 'temp': 1.01}, 'visibility': 10000, 'weather': [{'main': 'Clouds', 'icon': '04n', 'description': 'пасмурно', 'id': 804}], 'id': 524901, 'dt': 1478622600, 'cod': 200, 'name': 'Moscow', 'clouds': {'all': 90}}
forecast.json()['list'][0]:
{'dt': 1478628000, 'snow': {'3h': 0.027}, 'rain': {}, 'sys': {'pod': 'n'}, 'wind': {'deg': 288.501, 'speed': 2.57}, 'main': {'pressure': 1007.74, 'temp_kf': 2.39, 'temp_min': -2.84, 'humidity': 94, 'temp': -0.45, 'grnd_level': 1007.74, 'temp_max': -0.45, 'sea_level': 1028.51}, 'dt_txt': '2016-11-08 18:00:00', 'clouds': {'all': 80}, 'weather': [{'main': 'Clear', 'icon': '01n', 'description': 'ясно', 'id': 800}]}

'''

import requests
from datetime import datetime, timedelta
from tok import weather_key
#location = input('Локейшен-хуйешен: ') or 'Moscow'
base_url = 'http://api.openweathermap.org/data/2.5/weather'  #запрос для текущей погоды
forecast_url = 'http://api.openweathermap.org/data/2.5/forecast'  #прогноз на 5 дней с интервалом в 3 часа


def forecast_weather_format(data, when_day=None, when_time=None):
	pass

def forecast_weather_req(city, when_day=None, when_time=None):
	parameters = {'APPID': weather_key,
				  'units': 'metric',
				  'lang': 'ru'}
	if city == None:
		return 401
	else:
		parameters.update({'q': city})
		if when_day == when_time == None:
			current_weather = requests.get(base_url, parameters)
			temp_now = int(current_weather.json()['main']['temp'])
			loc_now = current_weather.json()['name']
			weather_description = current_weather.json()['weather'][0]['description']
			print (temp_now, loc_now, weather_description)
		else:
			forecast = requests.get(forecast_url, parameters)
			print(forecast.json()['city']['name'], forecast.json()['list'])
		#return forecast_weather_format(forecast.json()['list'], when_day, when_time)

#forecast_data = forecast.json()['list']  # список, данные по погоде на 5 дней


if __name__ == '__main__':
	print(forecast_weather_req(None, None, None))
	print(forecast_weather_req('Moscow'))
	print(forecast_weather_req('Taganrog', 1, 1))
	print(forecast_weather_req('Voronezh', 1))
	print(forecast_weather_req('Rostov'))
	'''
	print('Погода-хуегода в ', loc_now, temp_now, '\xB0С')
	print(current_weather.json())
	print(forecast.json()['list'][0])
	for i in range(len(forecast.json()['list'])):
		print('Температура на', datetime.fromtimestamp(forecast_data[i]['dt']), 'где-то', int(forecast_data[i]['main']['temp']), '\xB0С')  # \xB0С - символ градуса'''



