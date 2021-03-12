import pyowm
from pyowm.utils import config
from pyowm.utils import timestamps


owm = pyowm.OWM('42a62878cec9bcfc979975d7ef7f057c')

mgr = owm.weather_manager()

observation = mgr.weather_at_place('Sofia, BG')

w = observation.weather
m = w.temperature('celsius')

print(w)
print(m)