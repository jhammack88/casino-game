import random
print("Howdy! Welcome to Cowboy Slots!")

balance = 100

slot_options = {
    "7" : 10,
    "777" : 1,
    "Cherry": 8,
    "Grape" : 10,
    "Orange" : 5,
    "Apple" : 7
}

def spin_wheel(slot_options):
    reel1 = random.choices(list(slot_options.keys()), list(slot_options.values()))
    reel2 = random.choices(list(slot_options.keys()), list(slot_options.values()))
    reel3 = random.choices(list(slot_options.keys()), list(slot_options.values()))
    
    reels = [reel1[0], reel2[0], reel3[0]]
    print(reels)
    return reels
reels = spin_wheel(slot_options)

def winning(reels):
    if reels[0] == reels[1] and reels[2] == reels[1]:
        winnings = 5
    elif reels[0] == reels[1] or reels[2] == reels[0] or reels[1] == reels[2]:
        winnings = 3
    else: 
        winnings = 0
    print(winnings)
    return winnings

    

winning(reels)
