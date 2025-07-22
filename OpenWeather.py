#OpenWeather.py
#Joana Ugarte
#joanau@uci.edu
#44875730
# 454ee5d306e3309e1eaee620d185ee45

import urllib, json
from WebAPI import WebAPI


class OpenWeather(WebAPI):
    def __init__(self, zipcode="92617", ccode="US") -> None:
        self.zipcode = zipcode
        self.ccode = ccode
        self.temperature = 0
        self.high_temperature = 0
        self.low_temperature = 0
        self.longitude = 0
        self.latitude = 0
        self.description = ''
        self.humidity = ''
        self.sunset = ''
        self.city = ''


    def load_data(self) -> None:
        '''
        Calls the web api using the required values and stores the response in class data attributes.
            
        '''
        url = f"http://api.openweathermap.org/data/2.5/weather?zip={self.zipcode},{self.ccode}&appid={self.apikey}"
        w_obj = self._download_url(url)

        if w_obj is not None:
            self.temperature = (w_obj['main']['temp'])
            self.low_temperature = (w_obj['main']['temp_min'])
            self.high_temperature = (w_obj['main']['temp_max'])
            self.longitude = (w_obj['coord']['lon'])
            self.latitude = (w_obj['coord']['lat'])
            self.description = (w_obj['weather'][0]['description'])
            self.humidity = (w_obj['main']['humidity'])
            self.sunset = (w_obj['sys']['sunset'])
            self.city = (w_obj['name'])
            
    def transclude(self, message:str) -> str:
        '''
        Replaces keywords in a message with associated API data.
        :param message: The message to transclude
            
        :returns: The transcluded message
        '''
        msg = message.replace("@weather", self.description)
        return msg

