#!/usr/bin/env python
import sys,os

if(len(sys.argv)>3):
    print("Invalid number of arguments")
    exit(0)

if(len(sys.argv)==3):
    try:
        os.mkdir(sys.argv[2])
        print("Folder created:"+sys.argv[2])
        f = open(os.path.join(sys.argv[2],sys.argv[1]+".txt"),"w")
        f.close()
        os.system("subl "+sys.argv[2]+"/"+sys.argv[1]+".txt")
    except FileExistsError:
        os.chdir(sys.argv[2])
        if(os.path.isfile(sys.argv[1]+".txt")):
            os.system("subl "+sys.argv[1]+".txt")
        else:
            f = open(sys.argv[1]+".txt","w")
            f.close()
            os.system("subl "+sys.argv[1]+".txt")

if(len(sys.argv)==2):
    if(os.path.isfile(sys.argv[1]+".txt")):
        os.system("subl "+sys.argv[1]+".txt")
    else:
        f = open(sys.argv[1]+".txt","w")
        f.close()
        os.system("subl "+sys.argv[1]+".txt")