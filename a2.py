#a2.py

# Joana Ugarte
#joanau@uci.edu
#44875730
#The friendly one

import ui
from Profile import Profile
from Profile import Post
from pathlib import Path
import os.path

def C_com(p, inp): # C command, creates a new dsu file
    p = Path(p)
    extension = '.dsu'
    p = p.joinpath("{}{}".format(inp, extension)) # append a file name to the current path
    if not p.exists(): # check to see if file exists
      p.touch() # if file does not exist, create it
      print("New profile created:", p)
      profile.dsuserver = "localhost"
      username = input("Enter a username:")
      if ' ' in username:
          print("Error, whitespace in username.")
      else:
          profile.username = username
      password = input("Enter a password:")
      if ' ' in password:
          print("Error, whitespace in password.")
      else:
          profile.password = password
      bio = input("Please enter a bio:")
      profile.bio = bio
      profile.save_profile(str(p))
    else:
        print("File already exists.")
        if profile.username != None:
            print("The files username:", profile.username)
        else:
            print("Username does not exist.")
        if profile.password != None:
            print("The files password:", profile.password)
        else:
            print("Password does not exist.")
        if profile.bio != None:
            print("The files bio:", profile.bio)
        else:
            print("Bio does not exist.")

def O_com(file):
    p = Path(file)
    end = os.path.splitext(p)[1] #gets extension
    if end == '.dsu':
        if p.exists():
            if profile.username != None:
                print("The files username:", profile.username)
            else:
                print("Username does not exist.")
            if profile.password != None:
                print("The files password:", profile.password)
            else:
                print("Password does not exist.")
            if profile.bio != None:
                print("The files bio:", profile.bio)
            else:
                print("Bio does not exist.")
        else:
            print("ERROR. File cannot be loaded as it does not exist.")
    else:
        print("ERROR. File not DSU")

def E_com(file):
    p = Path(file)
    end = os.path.splitext(p)[1] #gets extension
    if end == '.dsu':
        if p.exists():
            euser = input("Great. Would you like to edit username?(enter yes or no)")
            if euser == 'yes':
                username = input("Cool. Please enter new username.")
                if ' ' in username:
                    print("Error, whitespace in username.")
                else:
                  profile.username = username
                  profile.save_profile(str(p))
            elif euser == 'no':
                print("That works too.")
            else:
                print("Unavailable option entered.")
            epwd = input("Would you like to edit Profile password?(enter yes or no)")
            if epwd == 'yes':
                password = input("Cool. Please enter new password.")
                if ' ' in password:
                    print("Error, whitespace in password.")
                else:
                    profile.password = password
                    profile.save_profile(str(p))
            elif epwd == 'no':
                print("That works too.")
            else:
                print("Unavailable option entered.")
            ebio = input("Would you like to edit Profile bio?(enter yes or no)")
            if ebio == 'yes':
                profile.bio = input("Cool. Please enter new bio.")
                profile.save_profile(str(p))
            elif ebio == 'no':
                print("That works too.")
            else:
                print("Unavailable option entered.")
            eadd = input("Would you like to add a post?(enter yes or no)")
            if eadd == 'yes':
                message = input("Great. Enter message now.")
                post.set_entry(message)
                profile.add_post(Post(message))
                profile.save_profile(str(p))
            elif eadd == 'no':
                print("That works too.")
            else:
                print("Unavailable option entered.")
            edel = input("Would you like to delete a post?(enter yes or no)")
            if edel == 'yes':
                num = input("Please enter id for post you want to delete.")
                profile.del_post(int(num))
                profile.save_profile(str(p))
            elif edel == 'no':
                print("That works too.")
            else:
                print("Unavailable option entered.")
        else:
            print("ERROR. File does not exist.")
    else:
        print("ERROR. File not DSU.")

        
def P_com(file):
    p = Path(file)
    end = os.path.splitext(p)[1] #gets extension
    if end == '.dsu':
        if p.exists():
            print("Which would you like to print?")
            print("1. Username")
            print("2. Password")
            print("3. Bio")
            print("4. Posts")
            print("5. Specific Post")
            print("6. All content")
            ans = input()
            if ans == '1':
                if profile.username != None:
                    print("The files username:", profile.username)
                else:
                    print("Username does not exist.")
            elif ans == '2':
                if profile.password != None:
                    print("The files password:", profile.password)
                else:
                    print("Password does not exist.")
            elif ans == '3':
                if profile.bio != None:
                    print("The files bio:", profile.bio)
                else:
                    print("Bio does not exist.")
            elif ans == '4':
                lposts = profile.get_posts()
                if len(lposts) == 0:
                    print("File has no posts.")
                else:
                    print("Posts:")
                    for i in lposts:
                        print(i)
            elif ans == '5':
                lposts = profile.get_posts()
                num = input("Please enter post id:")
                if (len(lposts) == 0) or (len(lposts) <= int(num)):
                    print("ID entered is not valid")
                else:
                    print(lposts[int(num)])
            elif ans == '6':
                lposts = profile.get_posts()
                if profile.username != None:
                    print("The files username:", profile.username)
                else:
                    print("Username does not exist.")
                if profile.password != None:
                    print("The files password:", profile.password)
                else:
                    print("Password does not exist.")
                if profile.bio != None:
                    print("The files bio:", profile.bio)
                else:
                    print("Bio does not exist.")
                if len(lposts) != 0:
                    print("Posts:")
                    for i in lposts:
                        print(i)
                else:
                    print("Profile has no posts.")
        else:
            print("ERROR. File does not exist.")
    else:
        print("ERROR. File not DSU")

opt = -1
profile = Profile()
post = Post()
while opt != "5":
    print("Welcome. Would you like to:")
    print("1. Create a Profile.")
    print("2. Open an existing Profile.")
    print("3. Edit a file.")
    print("4. Print info from file.")
    print("5. Quit")
    opt = input()
    if opt == '1':
        file = input("Please enter directory location.")
        name = input("Awesome. Please enter the name of new file.")
        C_com(file, name)
    elif opt == '2':
        file = input("Please enter file you would like to open.")
        O_com(file)
    elif opt == '3':
        file = input("Please enter file you would like to edit.")
        E_com(file)
    elif opt == '4':
        file = input("Please enter file you would like to print.")
        P_com(file)
    elif opt=="admin":
        print("running admin")
        ui.runadmin()

    
