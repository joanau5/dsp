#LastFM
#Joana Ugarte
#joanau@uci.edu
#44875730
#"f4b658c92bcb50c6f6cee59839891f63"
import urllib, json
from urllib import request, error
from WebAPI import WebAPI

class LastFM(WebAPI):
    def __init__(self, artist) -> None:
        self.artist = artist


    def load_data(self) -> None:
        '''
        Calls the web api using the required values and stores the response in class data attributes.
            
        '''
        url = f"http://ws.audioscrobbler.com/2.0/?method=artist.gettopalbums&artist={self.artist}&api_key={self.apikey}&format=json"
        m_obj = self._download_url(url)

        if m_obj is not None:
            self.topAlbums = m_obj['topalbums']['album'][0]['name']
            
    def transclude(self, message:str) -> str:
        '''
        Replaces keywords in a message with associated API data.
        :param message: The message to transclude
            
        :returns: The transcluded message
        '''
        msg = message.replace("@lastfm", self.topAlbums)
        return msg

