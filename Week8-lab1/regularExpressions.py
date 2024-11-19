import requests
response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Cork&appid=c3e26a0b5387b001f6f548f5710c0baf")
data = response.json()
temperature = data["main"]["temp"] - 273.15 # Kelvin to Celsius
print(f"Tramore Temp: {temperature}C")
print(f"Tramore Temp: {temperature}C")
