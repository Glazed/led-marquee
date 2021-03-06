import urllib.request
import json

def get():
	"""
	Returns properly formatted weather for Rochester, NY
	City can be changed by grabbing the proper openweathermap.org url.
	"""
	weather_string = "Weather Unavailable"

	weather_url = "http://api.openweathermap.org/data/2.1/weather/city/5134086"
	request = urllib.request.urlopen(weather_url)
	weather_info = json.loads(request.read().decode("utf-8"))
	if(request.getcode() not in range(200, 300)):
		request.close
		return weather_string
	request.close

	if weather_info is not None:
		temp = str(k_to_f(weather_info['main']['temp']))
		#state = str(weather_info['weather'][0]['main'])
		desc = str(weather_info['weather'][0]['description'])
		#weather_string = temp + " degrees, " + desc
		weather_string = temp + "°F, " + desc
	
	return weather_string

def k_to_f(kelvin):
	"""
	Returns Farenheit conversion from Kelvin
	"""
	return int((kelvin - 273.15)* 1.8000 + 32.0)

def isFiltered():                                                               
    """                                                                         
    Returns True if it must be filtered, False otherwise.                       
    """                                                                         
    return False
