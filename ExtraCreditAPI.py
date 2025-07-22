# ExtraCreditAPI.py
#Joana Ugarte
#joanau@uci.edu
#44875730
#nKamWDMDBleSMqkvIU6KRcnz491UShwxevORnFkL

# Mars Weather Service API

import urllib, json
from urllib import request, error
from WebAPI import WebAPI

global EXTRACREDITAPIKEY
EXTRACREDITAPIKEY = "nKamWDMDBleSMqkvIU6KRcnz491UShwxevORnFkL"

class ExtraCredit(WebAPI):
    def __init__(self) -> None:
        self.description = ''


    def load_data(self) -> None:
        '''
        Calls the web api using the required values and stores the response in class data attributes.
            
        '''
        url = f"https://api.nasa.gov/insight_weather/?api_key={self.apikey}&feedtype=json&ver=1."
        m_obj = self._download_url(url)

        if m_obj is not None:
            description = (m_obj['validity_checks']['1161']['AT']['sol_hours_with_data'][0])
            self.description = str(description)

    def transclude(self, message:str) -> str:
        '''
        Replaces keywords in a message with associated API data.
        :param message: The message to transclude
            
        :returns: The transcluded message
        '''
        msg = message.replace("@extracredit", self.description)
        return msg


