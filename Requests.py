import pyowm

owm = pyowm.OWM('42a62878cec9bcfc979975d7ef7f057c')

mgr = owm.weather_manager()

observation = mgr.weather_at_place('Rome, IT')

w = observation.weather
m = w.temperature('celsius')

print(w)
print(m)