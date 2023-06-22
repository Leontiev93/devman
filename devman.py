import requests


cities = [
    'Лондон',
    'Череповец',
    'svo'
]
params = {
    'TnMq': '',
    'lang': 'ru'
}


def request_the_weather(city, params=None):
    url = f'https://wttr.in/{city}'
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    return response.text


if __name__ == '__main__':
    for city in cities:
        print(request_the_weather(city, params))
