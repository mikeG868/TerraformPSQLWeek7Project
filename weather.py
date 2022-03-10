import requests

def get_weather(apikey,city):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(city,apikey)
    res = requests.get(url)
    data = res.json()
    return data['main']['temp']


if __name__ == '__main__':
    #API key
    with open("./DBignore.txt", 'r') as file:
        lines = [line.rstrip() for line in file]
    apikey = lines[3]

    city = 'helsinki'
    temp = get_weather(apikey,city)
    print('Temperature : {} degree celcius at {}'.format(temp,city))