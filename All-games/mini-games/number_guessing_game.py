import random


def guesser(no, attempts):
    while attempts > 0:
        print(f"you have {attempts} attempts to guess the number !")
        guess = int(input("make a guess: "))
        if guess < no:
            print("too low ! \n guess again!")
        elif guess > no:
            print("too high ! \n guess again!")
        else:
            print(f"congratulations! you guessed the number right! it was {no}")
            return
        attempts -= 1
    print(f"ooh no! you ran out of attempts... it was {no}")


number = random.randint(1, 100)
mode = input("choose difficulty : easy/hard : ").lower()
if mode == "easy":
    guesser(number, 10)
else:
    guesser(number, 5)
