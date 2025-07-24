import random

# computer choice
ch = int(random.randint(1,4))

# user choice
uc = int(input("enter 1 for rock , 2 for paper , and 3 for scissors"))

if (ch == 1 and uc == 3) or (ch == 2 and uc == 1) or (ch == 3 and uc == 2):
    print(f"the computer chose : {ch}")
    print("Computer wins! YOU LOSE")
elif ch == uc:
    print(" ITS A DRAW ! TRY AGAIN")
else:
    print("YOU WIN!! congratulations!!")