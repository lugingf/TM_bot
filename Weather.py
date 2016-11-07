#-*- coding: utf-8 -*-

'''
>>> payload = {'key1': 'value1', 'key2': 'value2'}
>>> r = requests.get('http://httpbin.org/get', params=payload)
>>> r.json()
>>> print(r.url)
http://httpbin.org/get?key1=value1&key2=value2&key2=value3
'''

import requests, json
location = input('Локейшен-хуйешен: ')
base_url = 'http://api.openweathermap.org/data/2.5/weather'

key = 'eb69b8a739a82912d62d8f6435655c97'
name = 'lugingf'

parameters = {'APPID' : key, 'q': location, 'units' : 'metric'}
connect = requests.get(base_url, parameters)

print('Погода-хуегода в ', connect.json()['name'], connect.json()['main']['temp'])


