from requests import get
import json

my_speech = 'из-за ремонта квартиры могу не успеть сдавать вовремя'

def show_parts(self):
    yandex_key = 'dict.1.1.20190505T195144Z.482f78e9f43c06ed.04709e9b874eda15dd753547107d7ea4e2dc8453'
    link = f"https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key={yandex_key}&lang=ru-en&&ui=ru&' \f'&flags=4&text="
    for words in (my_speech).split():
        result = get(f'{link}{words}').text
        print(f"{words} - {json.loads(result)['def'][0]['pos']}")

show_parts(my_speech)