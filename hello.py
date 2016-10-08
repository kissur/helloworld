import sys

def isname():
    global name
    if len(sys.argv) == 1: name = "World"
    else: name = sys.argv[1]

def hello ():
    print ("Hello " + name + "!")

isname()
hello()