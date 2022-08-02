from random import choices, randint
from time import sleep
from collections import Counter
from lib import approximateValue, goodbye, bye

playerName = str(input("""
Hello stranger,

Welcome in this mystery chamber!

What is your name ?

""")).title()

print(f"Hi {playerName}, lets the game begin\n")

goldInCrates = {
    'Green': [1000, 50],
    'Blue': [2000, 25],
    'Orange': [4000, 20],
    'Violet': [9000, 4],
    'Gold (LEGENDARY)': [16000, 1],
}

probability = []
for i in goldInCrates.values():
    probability.append(i[1])

cratesCollected = []
goldAcquired = 0
totalDiggingTime = 0


def game():
    crateProbability = {
        'reward': 60,
        'nothing': 40,
    }
    global cratesCollected, goldAcquired, totalDiggingTime

    gameLenght = int(input("How many steps you want to move?\n"))
    while gameLenght > 0:
        gameLenght -= 1
        playerMove = input("Do you want to go forward?\n").lower()
        if playerMove == "yes":
            print("Lets check what you found...\n")
            diggingTime = randint(0, 6)
            totalDiggingTime += diggingTime
            if diggingTime != 0:
                print(
                    f"You see something sticking out of the ground and you start digging for {diggingTime} seconds.\n")
            sleep(diggingTime)
            isCrateFound = choices(list(crateProbability.keys()), list(crateProbability.values()))[0]
            if isCrateFound == list(crateProbability.keys())[0]:
                whichCrateFound = choices(list(goldInCrates.keys()), probability)[0]
                print(
                    f"Excellent! You found {whichCrateFound} crate with {approximateValue(goldInCrates[whichCrateFound][0])} gold inside!\n")
                cratesCollected.append(whichCrateFound)
                goldAcquired += approximateValue(goldInCrates[whichCrateFound][0])
            else:
                print("Unlucky, there was nothing special!\n")
                continue

        else:
            askPlayAgain = str(input("""You just escaped the chamber and left all treasures inside
            Do you want to play again?"""))
            if askPlayAgain == "yes":
                game()
            break
    print(f"""
            End of path {playerName}

            You have found {len(cratesCollected)} {'crates' if len(cratesCollected) != 1 else 'crate'},""")
    for i in Counter(cratesCollected):
        print(f"""
            {i} crate: {Counter(cratesCollected)[i]}""")
    print(f"""
            You have {goldAcquired} gold in your pocket!

            You spent {totalDiggingTime} seconds digging!

            DO YOU WANT TO ENTER CHAMBER AGAIN ?""")
    again = input("\n").lower()
    if again == 'yes':
        game()
    goodbye(bye)


game()
