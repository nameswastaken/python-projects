import math
import time
import random
import socket

print("PYHTON PROGRAM GREEGEGEGEG")

iiiiu = input("Guess a num!").lower()
gambleresult = random.randint(1, 10)
hostname = socket.gethostname()
ipaddress = socket.gethostbyname(hostname)

if iiiiu == '5':
    print("GRAH")
elif iiiiu == '3.14':
    print("Pi? ", end="")
    print(math.pi)
elif iiiiu == '7':
    print("TIME TO GAMBLEEEEEEE")
    time.sleep(1)
    print("LETS SEE WHO WINS THIS TIME")
    time.sleep(0.5)
    print("...Spinning")
    time.sleep(2)
    print(f"{gambleresult}! ", end="")
    if gambleresult == 7:
        print("YOU WIN!!!!")
    elif gambleresult == 3:
        print("TREE!!! TREEEEE!!!!!!")
    else:
        print("FAIL! You're bankrupt now!")
elif iiiiu == '433':
    print("How the heck did you guess this?")
elif iiiiu == '18':
    print("i see, pick 7 on the next run")
elif iiiiu == '12624':
    print("yeah, today's date as of writing.")
elif iiiiu == '21':
    trueanswer = input("9+10?").lower()
    if trueanswer == '21':
        print("alright buddy")
        time.sleep(2)
        print("you're clearly either 2 years old")
        time.sleep(3)
        print("or you can't get over the joke")
        time.sleep(3)
        print("either way,")
        time.sleep(2)
        print(ipaddress)
    elif trueanswer == '19':
        print("yeah true but like")
        time.sleep(3)
        print("hm")
        time.sleep(2)
        print("check your closet")
    else:
        print("fail")
elif iiiiu == '1111111':
    print("ok")
elif type(iiiiu) == str:
    print("That isn't a number bro. (or it doesnt exist, idk how to fix)")
else:
    print("? run again..?")