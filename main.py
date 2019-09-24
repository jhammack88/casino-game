import random

print("Howdy! Welcome to Cowboy Slots!")
# print("Your current balance is $100\n")

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