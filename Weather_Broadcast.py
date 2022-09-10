#Weather_Broadcast, IP address finder, Location finder, Device name finder.
import requests, json
import socket 
hostname=socket.gethostname()  
def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

ip_address = get_ip()
response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
print("Your Device name is:",hostname)
print("Your IP Address:",ip_address)
print("City:",response.get("city"))
print("Region:",response.get("region"))
print ("Country:",response.get("country_name"))
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?" 
CITY =response.get("city").upper()
API_KEY = "5f9b5624d38a6f92307111e4f3261159" 
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY 
response = requests.get(URL) 
if response.status_code == 200:
     data = response.json()
     main = data['main'] 
     temperature = main['temp'] 
     temp_feel_like = main['feels_like'] 
     humidity = main['humidity'] 
     pressure = main['pressure'] 
     weather_report = data['weather'] 
     wind_report = data['wind'] 
     print(f"{CITY:-^35}") 
     print(f"City ID: {data['id']}") 
     print(f"Temperature: {temperature}") 
     print(f"Feel Like: {temp_feel_like}") 
     print(f"Humidity: {humidity}") 
     print(f"Pressure: {pressure}") 
     print(f"Weather Report: {weather_report[0]['description']}") 
     print(f"Wind Speed: {wind_report['speed']}") 
     print(f"Time Zone: {data['timezone']}") 
else: print("Error in the HTTP request")
