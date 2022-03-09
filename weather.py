import requests

#Db connection info
with open("./DBignore.txt", 'r') as file:
    lines = [line.rstrip() for line in file]
apikey = lines[3]

city = input('Enter your city : ')
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(city,apikey)
res = requests.get(url)
data = res.json()
temp = data['main']['temp']
print('Temperature : {} degree celcius at {}'.format(temp,city))
