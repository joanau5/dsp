# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Lucas Murray
# lomurray@uci.edu
# 25608000
#Joana Ugarte
#joanau@uci.edu
#44875730


import socket
import json
import Profile
import ds_protocol
import time
from NaClProfile import NaClProfile


def join(usr, pwrd, pubkey):
  join_msg = {"join": {"username": usr, "password": pwrd, "token": pubkey}}
  join_obj = json.dumps(join_msg)
  return join_obj

def postorbio(msg, token, choice):
  if msg and not msg.isspace():
    user = Profile.Post
    post_msg = {"token": token, choice: {"entry": msg,"timestamp": time.time()}}
    post_obj = json.dumps(post_msg)
    return post_obj

  else:
    newmsg = input('Input must contain characters; Please re-enter input:\n')
    return postorbio(newmsg, token, choice)
  
def send(server:str, port:int, username:str, password:str,  profobj, message:str, bio:str=None):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    try:
      client.settimeout(3)
      client.connect((server, port))
    except:
      print('INVALID PORT OR SERVER ADDRESS')
      return False


    send = client.makefile('w')
    recv = client.makefile('r')
    joincom = join(username, password, profobj.public_key)
    send.write(joincom)
    send.flush()
    resp = recv.readline()
    trans = ds_protocol.extract_json(resp)
    print(trans[0]['message'])
    print()

    if trans[1] == 'ok':
      usrtoken = trans[0]['token']
      if message != None:
        message = profobj.encrypt_entry(message, usrtoken)
        postcom = postorbio(message, profobj.public_key, "post")
        
        send.write(postcom)
        send.flush()
        resp = recv.readline()
        trans = ds_protocol.extract_json(resp)
        print(trans[0]['message'])
        print()

      if bio != None:
        bio = profobj.encrypt_entry(bio, usrtoken)
        biocom = postorbio(bio, profobj.public_key, "bio")
        send.write(biocom)
        send.flush()
        resp = recv.readline()
        trans = ds_protocol.extract_json(resp)
        print(trans[0]['message'])
        print()
      return True

    if trans[1] != 'ok':
      print(trans[0]['message'])
      return False



  
  '''
  The send function joins a ds server and sends a message, bio, or both

  :param server: The ip address for the ICS 32 DS server.
  :param port: The port where the ICS 32 DS server is accepting connections.
  :param username: The user name to be assigned to the message.
  :param password: The password associated with the username.
  :param message: The message to be sent to the server.
  :param bio: Optional, a bio for the user.
  '''

