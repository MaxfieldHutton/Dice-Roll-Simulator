import random
import matplotlib
matplotlibversion = matplotlib.__version__
import matplotlib.pyplot as plt
import numpy as np
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def print_info():
    cls()
    print("########################################")
    print("Element's Dice Roll Simulator ver: 1.0.1")
    print("matplotlib: " + matplotlibversion)
    print("numpy: "      + np.__version__)
    print("########################################\n\n")


print_info()

### dice_size is the amount of sides the dice have. EX: dice_size = 6, would be a D6
def get_dice_size():
    dice_size_chosen = False
    while not dice_size_chosen:
        try:
            dice_size_attempt = int(input("Please Enter the Dice Size (EX: 6 for a D6) \n"))
            if dice_size_attempt < 1:
                raise Exception("Input too small")
        except:
            cls()
            print("Invalid dice size, try again \n")
        else:
            dice_size_chosen = True
    return dice_size_attempt
 
dice_size = get_dice_size()
print_info()
print("Dice Size = " + str(dice_size))

### dice_amount will be how many dice we roll in a trial
def get_dice_amount():
    dice_amount_chosen = False
    while not dice_amount_chosen:
        try:
            dice_amount_attempt = int(input("Please Enter the amount of dice to roll in a trial \n"))
            if dice_amount_attempt < 1:
                raise Exception("Input too small")
        except:
            cls()
            print("Invalid dice amount, try again \n")
        else:
            print("Dice Amount = " + str(dice_amount_attempt))
            dice_amount_chosen = True
    return dice_amount_attempt
 
dice_amount = get_dice_amount()
print_info()
print("Dice Size = " + str(dice_size))
print("Dice Size = " + str(dice_amount))

### dice_trials will be how many times we roll a set of dice
def get_dice_trials():
    dice_trials_chosen = False
    while not dice_trials_chosen:
        try:
            dice_trials_attempt = int(input("Please Enter the amount of trials \n"))
            if dice_trials_attempt < 1:
                raise Exception("Input too small")
        except:
            cls()
            print("Invalid trial amount, try again \n")
        else:
            print("Trial Amount = " + str(dice_trials_attempt))
            dice_trials_chosen = True
    return dice_trials_attempt
 
dice_trials = get_dice_trials()
print_info()
print("Dice Size = "    + str(dice_size))
print("Dice Amount = "  + str(dice_amount))
print("Trial Amount = " + str(dice_trials))


total_output = []
for i in range(dice_trials):
    trial_output = []
    for j in range(dice_amount):
        trial_output.append(random.randrange(1, dice_size+1))
    total_output.append(sum(trial_output))
total_output.sort()


x_axis = []
for i in range(total_output[0], max(total_output)+1):
    ##  with 2 D6's this would be 2,3,4,5,6,7,8,9,10,11,12
    x_axis.append(i)

y_axis = []
for i in range(0, len(x_axis)):
    toAdd = 0
    for j in range(0, len(total_output)):
        if x_axis[i] == total_output[j]:
            toAdd += 1
    y_axis.append(toAdd)



plt.bar(x_axis, y_axis)
plt.show()