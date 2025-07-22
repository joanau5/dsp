#ui.py

# Joana Ugarte
# joanau@uci.edu
# 44875730

from Profile import Profile
from Profile import Post
from pathlib import Path
import os.path
# The not user friendly one, admin

def runadmin():
    def C_com(p, inp): # C command, creates a new dsu file
        p = Path(p)
        extension = '.dsu'
        p = p.joinpath("{}{}".format(inp, extension)) # append a file name to the current path
        if not p.exists(): # check to see if file exists
          p.touch() # if file does not exist, create it
          print(p, "created")
        else:
            print("File exists.")
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
            print("ERROR. File not dsu.")


    def E_com(file, inp):
        p = Path(file)
        end = os.path.splitext(p)[1] #gets extension
        if end == '.dsu':
            if '"' in inp:
                result = inp.split('"')
                for i in result:
                    if '-usr' in i:
                        num = result.index(i)
                        username = result[num+1]
                        if ' ' in username:
                            print("Error, whitespace in username.")
                        else:
                            profile.username = username
                            profile.save_profile(str(p))
                    if '-pwd' in i:
                        num = result.index(i)
                        password = result[num+1]
                        if ' ' in password:
                            print("Error, whitespace in password.")
                        else:
                            profile.password = password
                            profile.save_profile(str(p))
                    if '-bio' in i:
                        num = result.index(i)
                        profile.bio = result[num+1]
                        profile.save_profile(str(p))
                    if '-addpost' in i:
                        num = result.index(i)
                        message = result[num+1]
                        post.set_entry(message)
                        profile.add_post(Post(message))
                        profile.save_profile(str(p))
                    if '-delpost' in i:
                        index = i[-1]
                        lposts = profile.get_posts()
                        if len(lposts) > int(index):
                            profile.del_post(int(index))
                            profile.save_profile(str(p))
                        else:
                            print("ID entered is not valid")
            elif "'" in inp:
                result = inp.split("'")
                for i in result:
                    if '-usr' in i:
                        num = result.index(i)
                        username = result[num+1]
                        if ' ' in username:
                            print("Error, whitespace in username.")
                        else:
                            profile.username = username
                            profile.save_profile(str(p))
                    if '-pwd' in i:
                        num = result.index(i)
                        password = result[num+1]
                        if ' ' in password:
                            print("Error, whitespace in password.")
                        else:
                            profile.password = password
                            profile.save_profile(str(p))
                    if '-bio' in i:
                        num = result.index(i)
                        profile.bio = result[num+1]
                        profile.save_profile(str(p))
                    if '-addpost' in i:
                        num = result.index(i)
                        message = result[num+1]
                        post.set_entry(message)
                        profile.add_post(Post(message))
                        profile.save_profile(str(p))
                    if '-delpost' in i:
                        index = i[-1]
                        lposts = profile.get_posts()
                        if len(lposts) > int(index):
                            profile.del_post(int(index))
                            profile.save_profile(str(p))
                        else:
                            print("ID entered is not valid")
            else:
                result = inp.split()
                for i in result:
                    if '-usr' in i:
                        num = result.index(i)
                        username = result[num+1]
                        if ' ' in username:
                            print("Error, whitespace in username.")
                        else:
                            profile.username = username
                            profile.save_profile(str(p))
                    if '-pwd' in i:
                        num = result.index(i)
                        password = result[num+1]
                        if ' ' in password:
                            print("Error, whitespace in password.")
                        else:
                            profile.password = password
                            profile.save_profile(str(p))
                    if '-bio' in i:
                        num = result.index(i)
                        profile.bio = result[num+1]
                        profile.save_profile(str(p))
                    if '-addpost' in i:
                        num = result.index(i)
                        message = result[num+1]
                        post.set_entry(message)
                        profile.add_post(Post(message))
                        profile.save_profile(str(p))
                    if '-delpost' in i:
                        num = result.index(i)
                        index = num + 1
                        index = result[index]
                        lposts = profile.get_posts()
                        if len(lposts) > int(index):
                            profile.del_post(int(index))
                            profile.save_profile(str(p))
                        else:
                            print("ID entered is not valid")
        else:
            print("ERROR. File not dsu.")

    def P_com(file, inp):
        p = Path(file)
        end = os.path.splitext(p)[1] #gets extension
        if end == '.dsu':
            if '-usr' in inp:
                if profile.username != None:
                    print("The files username:", profile.username)
                else:
                    print("Username does not exist.")
            if '-pwd' in inp:
                if profile.password != None:
                    print("The files password:", profile.password)
                else:
                    print("Password does not exist.")
            if '-bio' in inp:
                if profile.bio != None:
                    print("The files bio:", profile.bio)
                else:
                    print("Bio does not exist.")
            if '-posts' in inp:
                lposts = profile.get_posts()
                if len(lposts) == 0:
                    print("File has no posts.")
                else:
                    print("Posts:")
                    for i in lposts:
                        print(i)
            if '-all' in inp:
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
            if '-post ' in inp:
                result = inp.split()
                num = result.index('-post')
                index = num + 1
                if len(result) > index:
                    lposts = profile.get_posts()
                    index = result[num+1]
                    if (len(lposts) > int(index)):
                        print(lposts[int(index)])
                    else:
                        print("ID entered is not valid")
                else:
                     print("Post index not included.")
        else:
            print("ERROR. File not dsu.")    

    inp = input()
    profile = Profile()
    post = Post()
    while inp != "Q":#until Q command is placed this will loop
        counter = 0
        if inp[0] == 'C':
            num = inp.index('-n')#finds index of first option in input
            partA = inp[:num]#splits input by where first option is and breaks after
            partB = inp[num:]
            partA = partA.split()
            partB = partB.split()
            nfile = partB[1]
            p = partA[1]
            C_com(p, nfile)
        elif inp[0] == 'O':
            file = inp[2:]
            O_com(file)
        elif inp[0] == 'E':
            print("What was the previously loaded file?")
            file = input()
            E_com(file, inp)
        elif inp[0] == 'P':
            print("What was the previously loaded file?")
            file = input()
            P_com(file, inp)
        else:
            print("ERROR")#if nothing applies then error occured
        inp = input()#loops untils Q is inputted





