import requests
city = "Moscow,RU"
appid = "cdf778b5f5669d8f94e12476be052125"
res = requests.get("http://api.openweathermap.org/data/2.5/forecast", params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nСредняя видимость <", '{0:3.0f}'.format(i['visibility']), "> \r\nСкорость ветра <", i['wind']['speed'], ">")
    print("____________________________")
