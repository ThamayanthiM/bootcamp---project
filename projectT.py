file=open("result.txt","w")
import requests
#import as
from datetime import datetime

api_key = "ac7883aaf53be3022172166fe14a1dc8"
location = input("Enter the city name: ")

complete_api_link ="http://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data["main"]["temp"]) -273.15)
weather_desc = api_data["weather"][0]["description"]
hmdt = api_data["main"]["humidity"]
wind_spd = api_data["wind"]["speed"]
date_time = datetime.now().strftime("%d %b %y | %I:%M:%S %p")
temp1 = "Weather stats for- {} || {}".format(location.upper(), date_time)
temp2 = "Current temperature is: {:.2f} deg C".format(temp_city)
temp3 = "Current weather desc :"+str(weather_desc)
temp4 = "Current Humidity     :"+str(hmdt)+'%'
temp5 = "Current wind speed   :"+str(wind_spd)+'kmph'
output ="---------------------------------------------------------------\n"+temp1+"---------------------------------------------------------------\n"+temp2+"\n"+temp3+"\n"+temp4+"\n"+temp5
print("---------------------------------------------------------------")
print("Weather stats for- {} || {}".format(location.upper(), date_time))
print("---------------------------------------------------------------")

print("Current temperature is: {:.2f} deg C".format(temp_city))
print("Current weather desc :",weather_desc)
print("Current Humidity     :",hmdt, '%')
print("Current wind speed   :",wind_spd, 'kmph')
file.write(output)
file.close()