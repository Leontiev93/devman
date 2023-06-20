import requests


cities = [
    'Лондон',
    'Череповец',
    'svo'
]

for city in cities:
    url = f'https://wttr.in/{city}?TnMq&lang=ru'
    response = requests.get(url=url)
    response.raise_for_status()
    print(response.text)
