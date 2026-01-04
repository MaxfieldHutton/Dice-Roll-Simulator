import random
import matplotlib
matplotlibversion: str = matplotlib.__version__
import matplotlib.pyplot as plt
import numpy as np
from colorama import Fore
from tqdm import tqdm
import os

def cls() -> None:
    os.system('cls' if os.name=='nt' else 'clear')

def print_info() -> None:
    cls()
    print(f"{Fore.CYAN}########################################")
    print("🎲 Element's Dice Roll Simulator 🎲 ver: 1.2.0")
    print("matplotlib: " + matplotlibversion)
    print("numpy: "      + np.__version__)
    print("########################################\n\n")


print_info()

### dice_size is the amount of sides the dice have. EX: dice_size = 6, would be a D6
def get_dice_size() -> int:
    dice_size_attempt = 0
    dice_size_chosen = False
    while not dice_size_chosen:
        try:
            dice_size_attempt = int(input(f"{Fore.WHITE}Please Enter the Dice Size (EX: 6 for a D6) \n"))
            if dice_size_attempt < 1:
                raise Exception("Input too small")
        except:
            cls()
            print(f"{Fore.YELLOW}Invalid dice size, try again {Fore.WHITE}\n")
        else:
            dice_size_chosen = True
    return dice_size_attempt
 
dice_size: int = get_dice_size()
print_info()
print(f"{Fore.GREEN}Dice Size = " + str(dice_size))

### dice_amount will be how many dice we roll in a trial
def get_dice_amount() -> int:
    dice_amount_attempt = 0
    dice_amount_chosen = False
    while not dice_amount_chosen:
        try:
            dice_amount_attempt = int(input(f"{Fore.WHITE}Please Enter the amount of dice to roll in a trial \n"))
            if dice_amount_attempt < 1:
                raise Exception("Input too small")
        except:
            cls()
            print(f"{Fore.YELLOW}Invalid dice amount, try again \n{Fore.WHITE}")
        else:
            print("Dice Amount = " + str(dice_amount_attempt))
            dice_amount_chosen = True
    return dice_amount_attempt
 
dice_amount: int = get_dice_amount()
print_info()
print(f"{Fore.GREEN}Dice Size = " + str(dice_size))
print(f"{Fore.GREEN}Dice Size = " + str(dice_amount))

### dice_trials will be how many times we roll a set of dice
def get_dice_trials() -> int:
    dice_trials_attempt = 0
    dice_trials_chosen = False
    while not dice_trials_chosen:
        try:
            dice_trials_attempt = int(input(f"{Fore.WHITE}Please Enter the amount of trials \n"))
            if dice_trials_attempt < 1:
                raise Exception("Input too small")
        except:
            cls()
            print(f"{Fore.YELLOW}Invalid trial amount, try again \n{Fore.WHITE}")
        else:
            print("Trial Amount = " + str(dice_trials_attempt))
            dice_trials_chosen = True
    return dice_trials_attempt
 
dice_trials: int = get_dice_trials()
print_info()
print(f"{Fore.GREEN}Dice Size = "    + str(dice_size))
print(f"{Fore.GREEN}Dice Amount = "  + str(dice_amount))
print(f"{Fore.GREEN}Trial Amount = " + str(dice_trials))

print(f"{Fore.WHITE} Doing Math: {Fore.CYAN}")
with tqdm(total=dice_trials) as pb:
    total_output: list[int] = []
    for i in range(dice_trials):
        trial_output: list[int] = []
        for j in range(dice_amount):
            trial_output.append(random.randrange(1, dice_size+1))
        total_output.append(sum(trial_output))
        pb.update()
    total_output.sort()


x_axis: list[int] = []
for i in range(total_output[0], max(total_output)+1):
    ##  with 2 D6's this would be 2,3,4,5,6,7,8,9,10,11,12
    x_axis.append(i)
    

y_axis: list[int] = []
print(f"{Fore.WHITE} Rendering: {Fore.BLUE}")
with tqdm(total=len(x_axis)) as pb:
    for i in range(0, len(x_axis)):
        toAdd = 0
        for j in range(0, len(total_output)):
            if x_axis[i] == total_output[j]:
                toAdd += 1
        y_axis.append(toAdd)
        pb.update()
        


plt.bar(x_axis, y_axis) # type: ignore
plt.show()              # type: ignore