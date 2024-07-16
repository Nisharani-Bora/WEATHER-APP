import requests

city_name = 'Assam'
API_key = '66c13160e5b906de53a84eef275bacc0'
url =f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'

response = requests.get(url)
if response.status_code == 200:

    data = response.json()
    print('Weather is', data['weather'][0]['description'])
    print('Current Temperature is', data['main']['temp'])
    print('Current Temperature Feels like is', data['main']['feels_like'])
    print('Current Humidity is', data['main']['humidity'])

