#-*- coding: utf-8 -*-

'''
>>> payload = {'key1': 'value1', 'key2': 'value2'}
>>> r = requests.get('http://httpbin.org/get', params=payload)
>>> r.json()
>>> print(r.url)
http://httpbin.org/get?key1=value1&key2=value2&key2=value3

'Конвертировать время POSIX в datetime'
print datetime.fromtimestamp(time.time())
#> 2010-08-14 02:58:15.057613

'Сдвинуть время'
print d + timedelta(days=1, hours=1)
#> 2010-08-15 03:58:15.057538

'Получиь день недели, 0 - Пн, 6 - Вс'
print d.weekday()
#> 5
'''

import requests
from datetime import datetime, timedelta
from tok import weather_key
location = input('Локейшен-хуйешен: ') or 'Moscow'
base_url = 'http://api.openweathermap.org/data/2.5/weather'  #запрос для текущей погоды
forecast_url = 'http://api.openweathermap.org/data/2.5/forecast'  #прогноз на 5 дней с интервалом в 3 часа
parameters = {'APPID' : weather_key,
			'q': location,
			'units' : 'metric',
			'lang': 'ru'}
connect = requests.get(base_url, parameters)
forecast = requests.get(forecast_url, parameters)


print('Погода-хуегода в ', connect.json()['name'], connect.json()['main']['temp'], '\xB0С')
print(connect.json())
print(forecast.json()['list'][0])
for i in range(len(forecast.json()['list'])-1):
	print('Температура на', forecast.json()['list'][i]['dt_txt'], 'где-то', int(forecast.json()['list'][i]['main']['temp']), '\xB0С')
	print('Timestamp', forecast.json()['list'][i]['dt'], 'это', datetime.fromtimestamp(forecast.json()['list'][i]['dt']), '\n')

