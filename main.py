import random
import matplotlib
matplotlibversion = matplotlib.__version__
import matplotlib.pyplot as plt
import numpy as np
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def printInfo():
    cls()
    print("########################################")
    print("Element's Dice Roll Simulator ver: 1.0")
    print("matplotlib: " + matplotlibversion)
    print("numpy: "      + np.__version__)
    print("########################################\n\n")


printInfo()

### DiceSize is the amount of sides the dice have. EX: DiceSize = 6, would be a D6
def GetDiceSize():
    DiceSizeChosen = False
    while not DiceSizeChosen:
        try:
            DiceSizeAttempt = int(input("Please Enter the Dice Size (EX: 6 for a D6) \n"))
        except:
            print("Invalid dice size, try again \n")
        else:
            DiceSizeChosen = True
    return DiceSizeAttempt
 
DiceSize = GetDiceSize()
printInfo()
print("Dice Size = " + str(DiceSize))

### DiceAmount will be how many dice we roll in a trial
def GetDiceAmount():
    DiceAmountChosen = False
    while not DiceAmountChosen:
        try:
            DiceAmountAttempt = int(input("Please Enter the amount of dice to roll in a trial \n"))
        except:
            print("Invalid dice amount, try again \n")
        else:
            print("Dice Amount = " + str(DiceAmountAttempt))
            DiceAmountChosen = True
    return DiceAmountAttempt
 
DiceAmount = GetDiceAmount()
printInfo()
print("Dice Size = " + str(DiceSize))
print("Dice Size = " + str(DiceAmount))

### DiceTrials will be how many times we roll a set of dice
def GetDiceTrials():
    DiceTrialsChosen = False
    while not DiceTrialsChosen:
        try:
            DiceTrialsAttempt = int(input("Please Enter the amount of trials \n"))
        except:
            print("Invalid trial amount, try again \n")
        else:
            print("Trial Amount = " + str(DiceTrialsAttempt))
            DiceTrialsChosen = True
    return DiceTrialsAttempt
 
DiceTrials = GetDiceTrials()
printInfo()
print("Dice Size = "    + str(DiceSize))
print("Dice Amount = "  + str(DiceAmount))
print("Trial Amount = " + str(DiceTrials))


TotalOutput = []
for i in range(DiceTrials):
    TrialOutput = []
    for j in range(DiceAmount):
        TrialOutput.append(random.randrange(1, DiceSize+1))
    TotalOutput.append(sum(TrialOutput))
TotalOutput.sort()


xAxis = []
for i in range(TotalOutput[0], max(TotalOutput)+1):
    ##  with 2 D6's this would be 2,3,4,5,6,7,8,9,10,11,12
    xAxis.append(i)

yAxis = []
for i in range(0, len(xAxis)):
    toAdd = 0
    for j in range(0, len(TotalOutput)):
        if xAxis[i] == TotalOutput[j]:
            toAdd += 1
    yAxis.append(toAdd)



plt.bar(xAxis, yAxis)
plt.show()