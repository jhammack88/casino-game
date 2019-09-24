import random

print("Howdy! Welcome to Cowboy Slots!")

balance = 100

ITEMS = ["BOOT", "HAT", "GUN", "SADDLE", "LASSO", "GOLD"]

slotOne = None
slotTwo = None
slotThree = None
stake = balance

def play():
    global stake, slotOne, slotTwo, slotThree
    playQuestion = askPlayer()
    while(stake != 0 and playQuestion == True):
        slotOne = spinWheel()
        slotTwo = spinWheel()
        slotThree = spinWheel()
        printScore()
        playQuestion = askPlayer()

def askPlayer():
    global stake
    while(True):
        answer = input("You have $" + str(stake) + ". Would you like to play? ")
        print("Please only use y or n to answer")
        answer = answer.lower()
        if(answer == "y"):
            return True
        elif(answer == "n"):
            print("This cowpokes ending balance is $" + str(stake) + ".")
            return False
        else:
            print("only y or n is accepted.")

