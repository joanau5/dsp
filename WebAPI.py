#WebAPI.py
#Joana Ugarte
#joanau@uci.edu
#44875730

from abc import ABC, abstractmethod
from urllib import request, error
import urllib, json
from urllib.error import HTTPError
import ssl

class WebAPI(ABC):

  def _download_url(self, url_to_download: str) -> dict:
    response = None
    r_obj = None

    try:
        ssl._create_default_https_context = ssl._create_unverified_context
        response = urllib.request.urlopen(url_to_download)
        json_results = response.read()
        r_obj = json.loads(json_results)

    except ConnectionError:
        print("Loss of local connection to the Internet.")

    except urllib.error.HTTPError as e:
        print('Failed to download contents of URL')
        if e.code == "404":
            print("Error 404 HTTP")
        if e.code == "503":
            print("Error 503 HTTP")
        print('Status code: {}'.format(e.code))
    
    except:
        print("Invalid use of API.")

    finally:
        if response != None:
            response.close()
    return r_obj
	
  def set_apikey(self, apikey:str) -> None:
    '''
        Sets the apikey required to make requests to a web API.
        :param apikey: The apikey supplied by the API service
            
    '''
    self.apikey = apikey
    
  @abstractmethod
  def load_data(self):
    pass
	
  @abstractmethod
  def transclude(self, message:str) -> str:
    pass
