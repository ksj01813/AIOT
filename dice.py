# dice.py
from random import randint

class Dice:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.value = 1
        self.size = 30
    def readDice(self):
        return  self.value
    def printDice(self):
        print(f"주사위의 값 = {self.value}")
    def rollDice(self):
        self.value = randint(1, 6)
d1 = Dice(100, 100)
d1.rollDice()
d1.printDice()
