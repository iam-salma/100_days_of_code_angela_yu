print("welcome to the Treasure island.\n your mission is to find the treasure.")
type1 = input("enter \"left\" or \"right\": ").lower()
if type1 == "right":
    print("Game Over! Try again")
    exit(0)
else:
    type2 = input("enter \"swim\" or \"wait\": ").lower()
    if type2 == "swim":
        print("Game Over! Try again")
        exit(0)
    else:
        type3 = input("specify the colour of door to enter \"yellow\" or \"red\" or \"blue\": ").lower()
        if type3 == "blue" or type3 == "red":
            print("Game Over! Try again")
            exit(0)
        else:
            print("You WIN !! congratulations!!")
