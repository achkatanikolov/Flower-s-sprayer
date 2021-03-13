class weather:
    def __init__(self, weather,temperature, humidity):
        self.__weather=weather
        self.__temperature = temperature
        self.__humidity = humidity
    def get_weather(self):
        return self.__weather
    def get_humidity(self):
        return self.__humidity
    def get_temperature(self):
        return self.__temperature
#import pyowm
#owm = pyowm.OWM('42a62878cec9bcfc979975d7ef7f057c')
#mgr = owm.weather_manager()
#observation = mgr.weather_at_place('Sofiq, BG')
#w = observation.weather
#m = w.temperature('celsius')
#z = w.wind()
#print(w)
#print(m)

#print(z)
import datetime
from datetime import date
date_object = datetime.date.today()
def leap(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return 1
            return 0
        return 1
weathers=[]
class Parametur_of_flowers:
    def __init__(self, amount_of_needed_of_water, type_of_soil, season, Weather, how_many_times, period_of_time, last_date_we_watered, current_date, where_to_plant):
        self.__amount_of_needed_of_water = amount_of_needed_of_water
        self.__type_of_soil = type_of_soil
        self.__season = season
        self.__weather = Weather
        self.__how_many_times_a_week = how_many_times
        self.__period_of_time = period_of_time
        self.__last_date_we_watered = last_date_we_watered
        self.__current_date = current_date
        self.__where_to_plant = where_to_plant
    def new_date(self,date):
        self.__current_date=date
    def when_to_water_the_plant(self):
        how_much_water_in_the_end=self.__amount_of_needed_of_water
        a=self.__current_date - self.__last_date_we_watered
        if a.days == self.__period_of_time:
            self.__last_date_we_watered=self.__current_date
            if weather.get_weather(self.__weather)=="rainy":# or weathers[len(weathers)-1]=="rainy":
                weathers=[]
                weathers.append(self.__weather)
                return 
            if weather.get_humidity(self.__weather)>=50 and weather.get_humidity(self.__weather)<70:
                how_much_water_in_the_end-=how_much_water_in_the_end/100
            elif weather.get_humidity(self.__weather)>=70:
                how_much_water_in_the_end-=how_much_water_in_the_end*2/100
            if weather.get_temperature(self.__weather)<13:
                how_much_water_in_the_end-=how_much_water_in_the_end*1.5/100
        if round(how_much_water_in_the_end)==0:
            return how_much_water_in_the_end
        else:
            return round(how_much_water_in_the_end)
    def get_weather(self):
        return weather.get_weather(self.__weather)
#weathers={"rainy":weather(7,10,2,0,True,0),"rainy_and_windy":weather(4,10,2,1,1,0),"cloudy":(15,10,2,0,False,0),"cloudy_and_windy":(15,10,2,1,False,0),"cloudy_and_sunny":(13,10,1,0,False,1),"cloudy_windy_and_sunny":weather(9,10,1,1,False,1),"sunnny":weather(20,10,0,0,False,2),"sunny_and_windy":weather(18,10,0,1,False,2)}
lavandula=Parametur_of_flowers(50,"chernozemna","S",weather("sunny",12,75),1,7,datetime.date.today(),datetime.date.today(),"soil")
weathers.append(Parametur_of_flowers.get_weather(lavandula))
Parametur_of_flowers.new_date(lavandula,date(2021,3,20))
Parametur_of_flowers.when_to_water_the_plant(lavandula)



