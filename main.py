import random

slot_options = {
    "7" : 3,
    "777" : 1,
    "CowboyHat": 8,
    "Pistol" : 10,
    "Saddle" : 5,
    "Lasso" : 7
}

def spin_wheel(slot_options, bet):
    global user_wallet
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
        winning(reels, slot_options)
        return reels


def winning(reels, slot_options):
    global user_wallet
    if reels[0] == reels[1] and reels[2] == reels[1]:
        winnings = 300 * (.5 / slot_options[reels[0]])
        print(f"You WIN!! ...${winnings:.2f}")
    elif reels[0] == reels[1] or reels[2] == reels[0]:
        winnings = 200 * (1 / slot_options[reels[0]])
        print(f"You WIN!! ...${winnings:.2f}")
    elif reels[1] == reels[2]:
        winnings = 100 * (1 / slot_options[reels[1]])
        print(f"You WIN!! ...${winnings:.2f}")
    else: 
        winnings = 0
        print(f"Sorry you booty!")
    user_wallet += winnings  
     
    
    print(f"Your new balance is ...${user_wallet:.2f}")
    nav()
    return winnings

def nav():
    global user_wallet
    user_choice = input("What would you like to do? \n 1: Spin Wheel \n 2: Check Balance \n 3: Add Funds \n 4: Cash Out\n")
    if user_choice == "1":
        reels = spin_wheel(slot_options, bet)
    elif user_choice == "2":
        print(f"Your current balance is.. ${user_wallet:.2f}")
        nav()
    elif user_choice == "3":
        wallet()
    elif user_choice == "4":
        print(f"Thanks! Your final balance is.. ${user_wallet:.2f}") 
        exit()

    

def wallet():
    global user_wallet
    add_money = input("How much would you like to add?\n $")
    if add_money.isnumeric() == True:
        user_wallet += float(add_money)
        print(f"Your new balance is... ${user_wallet:.2f}")
        nav()
    else: 
        print("Invalid Input")
        wallet()
    

print("Howdy! Welcome to Cowboy Slots!")
user_wallet = float(input("How much would you like to add?\n $"))
bet = float(input("How much would you like to bet?\n $"))
reels = spin_wheel(slot_options, bet)





