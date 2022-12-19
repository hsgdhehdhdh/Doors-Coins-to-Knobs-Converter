def convert(c, k):
    k = int(0)
    c = int(c)
    k = int(c) // int(20)
    k = str(k)
    c = str(c)
    if int(k) == 1:
        print(c + " coins will give you 1 extra knob")
    else:
        if int(k) == 0:
            print(c + " coins will give you no extra knobs")
        else:
            print(c + " coins will give you " + k + " extra knobs")
    input("press enter to close program")
    quit()
def retrycoins():
    print("You must enter a number")
    getcoins("coins")
def getcoins(c):
    c = input("How many coins do you have?: ")
    if c.isnumeric() == True:
        c = int(c)
        convert(c, 0)
    else:
        if c.isnumeric() == False:
            retrycoins()
def start():
    print("Roblox Doors Coins > Knobs converter v1.0")
    getcoins("coins")
start()
