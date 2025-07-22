#a2.py

# Joana Ugarte
#joanau@uci.edu
#44875730
#ui3.py

from ExtraCreditAPI import ExtraCredit
from LastFM import LastFM
from OpenWeather import OpenWeather
from Profile import Profile
from Profile import Post
from pathlib import Path
import ds_client
import os.path
import WebAPI


def test_api(message:str, apikey:str, webapi:WebAPI):
  webapi.set_apikey(apikey)
  webapi.load_data()
  result = webapi.transclude(message)
  return result

def biochange(bio1, profile):
    if bio1 == "yes":
        bio1 = input("Enter new bio:")
        profile.bio = bio1 
        profile.save_profile(str(p))
        return True
    elif bio1 == "no":
        print("Okay no bio change.")
    else:
        print("Invalid command entered.")


def run(server, profile, post):
    username = input("Please enter username.")
    password = input("Please enter password.")
    bio = ""
    message = ""
    extension = '.dsu'
    global p
    p = Path(str(Path.cwd())+"/"+username+".dsu")
    if p.exists():
        profile.dsuserver = server
        if profile.username != None:
            username = profile.username
        if profile.password != None:
            password = profile.password
        if profile.bio != None:
            bio = profile.bio
        d = ds_client.send(server, 3021, username, password, message, bio)
        if d == 'Invalid password or username already taken':
            print("Incorrect password.")
            return
            
    else:
        p.touch()
        profile.dsuserver = server
        profile.username = username
        profile.password = password
        profile.save_profile(str(p))
        ds_client.send(server, 3021, username, password, message, bio)
        
    bio1 = input("Do you want to change bio?(yes or no)")
    state = biochange(bio1, profile)
    if state == True:
        ds_client.send(server, 3021, username, password, message, profile.bio)

    posts = input("Would you like to add a post?(yes or no)")
    if posts == "yes":
        apis = input("Would you like to use a keyword?(yes or no")
        if apis == "yes":
            print("@weather can be used to tell the weather." )
            print("@lastfm can be used to find artists top album.")
            print("@extracredit can be used to tell mars weather.")
            message = input("Enter your post:")
            if "@weather" in message:
                apikey = input("Please enter apikey for weather.")
                message = test_api(message, apikey, OpenWeather())
            if "@lastfm" in message:
                apikey = input("Please enter apikey for lastfm.")
                artist = input("Please enter artist.")
                message = test_api(message, apikey, LastFM(artist))
            if "@extracredit" in message:
                apikey = input("Please enter apikey for extra.")
                message = test_api(message, apikey, ExtraCredit())
            post.set_entry(message)
            profile.add_post(Post(message))
            profile.save_profile(str(p))
            ans = input("Would you like to publish this online?(yes or no)")
            if ans == "yes":
                ds_client.send(server, 3021, username, password, message, bio)
            elif ans == "no":
                print("Okay, post was not published.")
            else:
                print("Invalid command.")
        else:
            print("Okay. Moving on.")
            message = input("Enter your post:")
            post.set_entry(message)
            profile.add_post(Post(message))
            profile.save_profile(str(p))
            ans = input("Would you like to publish this online?(yes or no)")
            if ans == "yes":
                ds_client.send(server, 3021, username, password, message, bio)
            elif ans == "no":
                print("Okay, post was not published.")
            else:
                print("Invalid command.")
    else:
        print("No changes to post.")



    
    
