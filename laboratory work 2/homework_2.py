import requests
city = "Moscow,RU"
appid = "cdf778b5f5669d8f94e12476be052125"
res = requests.get("http://api.openweathermap.org/data/2.5/weather", params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Город:", city)
print("Средняя видимость:", data['visibility'])
print("Скорость ветра:", data['wind']['speed'])
