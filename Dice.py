import random

class Dice:
    def rollDice(self):
        randomNum = random.randint(1,6)
        print("")
        print(f'You rolled : {randomNum}')
        return randomNum
