import requests


cities = [
    'Лондон',
    'Череповец',
    'svo'
]
params = {
    'lang': 'ru',
}


def response_weather(cities, params=None):
    for city in cities:
        url = f'https://wttr.in/{city}?TnMq'
        response = requests.get(url=url, params=params)
        response.raise_for_status()
        print(response.text)


response_weather(cities, params)
