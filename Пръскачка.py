#class weather:
    #def __init__(self, temprature, humdity, cloudiness, windiness, is_it_rainy, sunniness):
        #self.__temprature = temprature
        #self.__humdity = humdity
        #self.__cloudiness = cloudiness
        #self.__windiness = windiness
        #self.__is_it_rainy = is_it_rainy
import datetime
date_object = datetime.date.today()
print(date_object)
class Parametur_of_flowers:
    def __init__(self,need_of_water,type_of_soil,Weather,last_day_that_flower_was_watered):
        self.__need_of_water = need_of_water
        self.__type_of_soil = type_of_soil
        self.__weather = Weather
        self.__last_day_that_flower_was_watered=last_day_that_flower_was_watered
    def when_to_water_plant(self):

#weathers={"rainy":weather(7,10,2,0,True,0),"rainy_and_windy":weather(4,10,2,1,1,0),"cloudy":(15,10,2,0,False,0),"cloudy_and_windy":(15,10,2,1,False,0),"cloudy_and_sunny":(13,10,1,0,False,1),"cloudy_windy_and_sunny":weather(9,10,1,1,False,1),"sunnny":weather(20,10,0,0,False,2),"sunny_and_windy":weather(18,10,0,1,False,2)}
#flowers={"orhideq":Parametur_of_flowers(2,100), "mak":Parametur_of_flowers(5,50)}