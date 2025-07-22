# a3.py

# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Joana Ugarte
# joanau@uci.edu
# 44875730

import ds_client
import ui3
from Profile import Profile
from Profile import Post


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
    
