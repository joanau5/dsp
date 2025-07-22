#a1.py

from pathlib import Path
import os.path

def L_com(path): # L command lists objects in path
    p = Path(path)
    file2 = []
    directory = []
    for obj in p.iterdir(): #loops through to find files
      if obj.is_file():
          file2.append(obj)
      elif obj.is_dir(): # loops through to find directory
          directory.append(obj)
    for i in file2:
        print(i)
    for j in directory:
        print(j)

def F_opt(p): # F option prints only files
    p = Path(p)
    for obj in p.iterdir(): # loops through to find files
      if obj.is_file():
          print(obj)

def S_opt(p, inp): # S option: checks if file document exists
    p = os.path.join(p, inp) #adds path & file together regardless if Windows or Posix
    pathf = Path(p)
    if pathf.exists(): #check to see if path exists
        print(p)
    else:
        print("Error file does not exist.")

def E_opt(p, extension): # E option, prints files with specific extension
    p = Path(p)
    extension = '.{}'.format(extension) #adds period to inputed extension
    for obj in p.iterdir(): #iterates through path to check for file with extension
        extt = os.path.splitext(obj)[1] #gets obj extension
        if extt == extension: # checks if matches inputed extension
            print(obj)

def R_opt(sumt): #R option, recursively prints objective
    p = Path(sumt)
    for obj in p.iterdir():
        if obj.is_file():# if simplified to file it will be
            print(obj)
    for obj in p.iterdir():
        if obj.is_dir():
            print(obj)
            R_opt(obj)#recursion, runs through own function

def C_com(p, inp): # C command, creates a new dsu file
    p = Path(p)
    extension = '.dsu'
    p1 = p.joinpath("{}{}".format(inp, extension)) # append a file name to the current path

    if not p1.exists(): # check to see if file exists
      p1.touch() # if file does not exist, create it
    print(p1)

def D_com(file): # D command, deletes a file
    rf = Path(file)
    end = os.path.splitext(rf)[1] #checks extension 
    if end == '.dsu': #makes sure correct extension is being used
        rf.unlink(file)
        print(file, "DELETED")
    else:
        print("ERROR")#error if path does not have .dsu extension

def R_com(file): # R command
    rf = Path(file)
    end = os.path.splitext(rf)[1] #gets path extension
    if end == '.dsu' :
        if os.path.getsize(file) == 0: #if file size is 0 it is empty
            print("EMPTY")
        else:
            f = rf.open('r')
            cleanr = ""
            for line in f: #print files content without newline 
                nline = line.strip()
                cleanr += nline
            print(nline)
            f.close()
    else:
        print("ERROR") #if not .dsu extension it will cause error

def rf_combo(p): # options r and f combined
    p = Path(p)
    for obj in p.iterdir(): 
        if obj.is_file():# if obj is file it will be printed
            print(obj)
    for obj in p.iterdir():
        if obj.is_dir():
            R_opt(obj) #recursive call, directory will not be printed but placed into function

def re_combo(sumt): #options r and e combined
    extension = partB[2] #gets specific inputted extension
    extension = '.{}'.format(extension)
    p = Path(sumt)
    for obj in p.iterdir():
        ex = os.path.splitext(obj)[1]#gets obj extension
        if obj.is_file() and extension == ex: #if it is a file and extension is the same as inputted it will print
            print(obj)
    for obj in p.iterdir():
        if obj.is_dir():
            re_combo(obj)# recursive call, directory placed back into function

    
def rs_combo(p, inp):# options r and s combined
    p = Path(p)
    for obj in p.iterdir():
        if inp in str(obj): #if inputted string is in obj it is the file being searched
            print(obj)
    for obj in p.iterdir():
        if obj.is_dir():
            rs_combo(obj, inp)#recursive call to search for file if in a directory
            
if __name__ == '__main__':
    options = ['-r','-f','-s', '-e', '-n']#all the different options
    inp = input()
    while inp != "Q":#until Q command is placed this will loop
        counter = 0
        for i in options:
            if i in inp:
                counter += 1#counts how many options are being dealt with
        for i in options:
            if i in inp:
                num = inp.index(i)#finds index of first option in input
                partA = inp[:num]#splits input by where first option is and breaks after
                partB = inp[num:]
                partA = partA.split()
                partB = partB.split()
                break
        if len(inp) < 5:#if less than 5 characters long it is unlikely to be valid input
            print("ERROR")
        elif counter == 0:# if no options are in input, then these are the only commands possible
            if inp[0] == 'D':
                file = inp[2:]
                D_com(file)
            elif inp[0] == 'L':
                file = inp[2:]
                L_com(file)
            elif inp[0] == 'R':
                file = inp[2:]
                R_com(file)
        elif counter == 1:# if only one option was used then these are only possible commands
            if partA[0] == 'C':
                if partB[0] =='-n':# only -n option can be used with C
                    nfile = partB[1]
                    p = partA[1]
                    C_com(p, nfile)
            elif partA[0] == 'L':#all possible options for L command
                if partB[0] == '-f': #if f only files should be printed
                    p = partA[1]
                    F_opt(p)
                elif partB[0] == '-s':#if s only specific file should be printed
                    sfile = partB[1]
                    pa = partA[1]
                    S_opt(pa, sfile)
                elif partB[0] == '-e':#if e only files with specific input should be printed
                    extension = partB[1]
                    pa = partA[1]
                    E_opt(pa, extension)
                elif partB[0] == '-r':#if r, path will be printed recursively
                    p = partA[1]
                    R_opt(p)
        elif counter == 2:# if two options then it will be one of these possible combinations
            if '-r' and '-f' in inp:
                p = partA[1]
                rf_combo(p)
            if '-r' and '-e' in inp:
                p = partA[1]
                re_combo(p)
            if '-r' and '-s' in inp:
                p = partA[1]
                inpu = partB[2]
                rs_combo(p, inpu)
        else:
            print("ERROR")#if nothing applies then error occured
        inp = input()#loops untils Q is inputted


