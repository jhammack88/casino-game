import random
print("Howdy! Welcome to Cowboy Slots!")

user_wallet = 0

slot_options = {
    "7" : 10,
    "777" : 1,
    "Cherry": 8,
    "Grape" : 10,
    "Orange" : 5,
    "Apple" : 7
}

def spin_wheel(slot_options):
    global user_wallet
    bet = float(input("How much would you like to bet? $"))
    if user_wallet < bet:
        print("NOT enough skins bro!!")
        wallet()
    else:
        reel1 = random.choices(list(slot_options.keys()), list(slot_options.values()))
        reel2 = random.choices(list(slot_options.keys()), list(slot_options.values()))
        reel3 = random.choices(list(slot_options.keys()), list(slot_options.values()))
        
        reels = [reel1[0], reel2[0], reel3[0]]
        user_wallet -= bet
        print(reels)
        winning(reels)
        return reels


def winning(reels):
    global user_wallet
    if reels[0] == reels[1] and reels[2] == reels[1]:
        winnings = 5
    elif reels[0] == reels[1] or reels[2] == reels[0] or reels[1] == reels[2]:
        winnings = 3
    else: 
        winnings = 0
    user_wallet += winnings    
    print(f"${winnings}")
    print(f"${user_wallet}")
    nav()
    return winnings

def nav():
    global user_wallet
    user_choice = input("what would you like to do? \n 1: Spin Wheel \n 2: Check Balance \n 3: Cash Out \n")
    if user_choice == "1":
        reels = spin_wheel(slot_options)
    elif user_choice == "2":
        print(f"your current balance is.. ${user_wallet}")
        nav()
    elif user_choice == "3":
        print(f"Thanks! Your final balance is.. ${user_wallet}") 
        exit()

def wallet():
    global user_wallet
    add_money = input("How much would you like to add? $")
    if add_money.isnumeric() == True:
        user_wallet += float(add_money)
        nav()
    else: 
        print("Invalid Input")
        wallet()
    


wallet()





