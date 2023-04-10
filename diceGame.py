import time as t
import random as r

# loop var
isShop = True
isRolling = True

# Dice var
diceMin = 1
diceMax = 6
multiplier = 1
amtOfDice = 1
maxRolls = 2
points = 0

# Cost var
minCost = 30
maxCost = 75
multiCost = 225
amtCost = 150
maxRollsCost = 250

# Cost multiplier var
minCostMulti = 2
maxCostMulti = 2.5
multiCostMulti = 2
amtCostMulti = 3.5
maxRollsCostMulti = 3.5

class bcolors:
    red = '\033[91m'
    blue = '\033[96m'
    green = '\033[92m'
    end = '\033[0m'
    bold = '\033[1m'

print(bcolors.bold + "How to play:" + bcolors.end)
t.sleep(0.75)
print(bcolors.red + "Step 1: choose how many iterations of dice you want to roll" + bcolors.end)
t.sleep(0.75)
print(bcolors.blue + "Step 2: Use your new found points for upgrades, or reroll your dice" + bcolors.end)
t.sleep(0.75)
print(bcolors.green + "Step 3: repeat steps 1 and 2 until you have an unimaginable amount of money" + bcolors.end)
t.sleep(0.75)
print(bcolors.bold + "NOTE: amt of rolls and amt of dice affects time to gain points e.g 100 rolls and dice takes 15 seconds, 1 roll and dice takes 0.15 seconds" + bcolors.end)
t.sleep(1)

print("\n")

def randomInsult():
    randomInt = r.randint(0, 2)

    if(randomInt == 0):
        print(bcolors.bold + bcolors.red + "\nBro, is a number that hard to type." + bcolors.end)
    elif(randomInt == 1):
        print(bcolors.bold + bcolors.red + "\nCan you not listen to instructions. Honestly." + bcolors.end)
    elif(randomInt == 2):
        print(bcolors.bold + bcolors.red + "\nWhy can you not follow simple instructions." + bcolors.end)


def roll():
    global points, isRolling

    iterations = 0
    iterationsReset = 0
    pointGain = 0

    while(isRolling):
        try:
            iterations = int(input(bcolors.bold + "How many times do you want to roll your " + str(amtOfDice) + " dice up to " + str(maxRolls) + " times (type 0 to stop rolling): " + bcolors.end))
            iterationsReset = iterations
        except(ValueError):
            randomInsult()

        if(iterations != 0):
            if(iterations <= maxRolls):
                for i in range(amtOfDice):
                    while(iterations > 0):
                        pointGain += r.randint(diceMin, diceMax) * multiplier
                        iterations -= 1
                    iterations = iterationsReset
            else:
                print(bcolors.bold + "My friend... I said up to " + str(maxRolls) + bcolors.end)

            t.sleep((iterations/10) + (amtOfDice/20))

            print(bcolors.green + "\nyou gained: $" + str(pointGain) + bcolors.end)
            points += pointGain
            pointGain = 0
        else:
            isRolling = False

    isRolling = True



def shop():
    global points, diceMin, diceMax, multiplier, amtOfDice, maxRolls, minCost, maxCost, multiCost, amtCost, maxRollsCost, isShop

    print(bcolors.bold + "\nDo you want to go to the shop, or re-roll" + bcolors.end)

    if(points < min(minCost, maxCost, multiCost, amtCost, maxRollsCost)):
        print(f"{bcolors.bold}{bcolors.red}You can not afford anything{bcolors.end}")
    
    sorr = input(bcolors.bold + "Type S for shop, R for re-roll: " + bcolors.end)
    print(bcolors.green + "\npoints: " + str(points) + bcolors.end)

    if(sorr.lower() == "s" or sorr.lower() == "shop"):

        print(bcolors.red + "\nDice minimum value = " + str(diceMin) + "\nDice maximum value = " + str(diceMax) + "\nDice multiplier = " + str(multiplier) + bcolors.end)

        while(isShop):
            option = ""

            print(bcolors.green + "\npoints: " + str(points) + bcolors.end)
            print(f"\n What would you like to upgrade: {bcolors.blue} \n 1. dice minimum value: ${minCost} \n 2. dice maximum value: ${maxCost} \n 3. roll multiplier: ${multiCost} \n 4. amount of dice: ${amtCost} \n 5. max roll amount ${maxRollsCost} \n 6. leave {bcolors.end}")

            
            try:
                option = int(input(bcolors.bold + "\nType the number of the associated option: " + bcolors.end))
                print("\n")
            except (ValueError):
                print(bcolors.red + "\nDude I said a number..." + bcolors.end)

            if(option == 1):
                if(diceMin < diceMax):
                    if(points >= minCost):
                        points -= minCost
                        minCost = round(minCost * minCostMulti)
                        diceMin += 1
                        print(f"{bcolors.bold}New dice min: {diceMin}{bcolors.end}")
                    else:
                        print(f"{bcolors.bold}You gotta have enough money!{bcolors.end}")
                else:
                    print(f"{bcolors.red}Min dice value can not be greater than the max value{bcolors.end}")

            elif(option == 2):
                if(points >= maxCost):
                    points -= maxCost
                    maxCost = round(maxCost * maxCostMulti)
                    diceMax += 1
                    print(f"{bcolors.bold}New dice max: {diceMax}{bcolors.end}")
                else:
                    print(f"{bcolors.bold}You gotta have enough money!{bcolors.end}")

            elif(option == 3):
                if(points >= multiCost):
                    points -= multiCost
                    multiCost = round(multiCost * multiCostMulti)
                    multiplier += 1
                    print(f"{bcolors.bold}New dice multiplier: {multiplier}{bcolors.end}")
                else:
                    print(f"{bcolors.bold}You gotta have enough money!{bcolors.end}")

            elif(option == 4):
                if(points >= amtCost):
                    points -= amtCost
                    amtCost = round(amtCost * amtCostMulti)
                    amtOfDice += 1
                    print(f"{bcolors.bold}New dice amount: {amtOfDice}{bcolors.end}")
                else:
                    print(f"{bcolors.bold}You gotta have enough money!{bcolors.end}")

            elif(option == 5):
                if(points >= maxRollsCost):
                    points -= maxRollsCost
                    maxRollsCost = round(maxRollsCost * maxRollsCostMulti)
                    maxRolls += 1
                    print(f"{bcolors.bold}New dice rolls: {maxRolls}{bcolors.end}")
                else:
                    print(f"{bcolors.bold}You gotta have enough money!{bcolors.end}")
            
            elif(option == 6):
                isShop = False

            else:
                randomInsult()


    elif(sorr.lower() == "r"or sorr.lower() == "rereoll"or sorr.lower() == "re-roll"):
        pass

    else:
       randomInsult()

    isShop = True





while(True):
    roll()
    shop()