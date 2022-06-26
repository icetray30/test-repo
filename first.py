import requests
response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=London&APPID=323a805c82f4e444c4d6eb02dd3")
print(response.text)