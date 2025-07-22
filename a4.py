#a4.py
#Joana Ugarte
#joanau@uci.edu
#44875730

import urllib, json
import ds_client
import ui3
from Profile import Profile
from Profile import Post
from urllib import request,error
import json
from OpenWeather import OpenWeather 
from LastFM import LastFM
from ExtraCreditAPI import ExtraCredit
import WebAPI

profile = Profile()
post = Post()
server = input("Please enter server.")
while True:
   try:
       ui3.run(server, profile, post)
       cont = input("Would you like to keep going?(Y or N)")
       if cont == 'N':
           break
       elif cont == 'Y':
           continue
       else:
           print('Incorrect commmand.')
   except:
       print("Unforseen error occured.")
