import random

words = ["potato", "carrot", "tomato", "cauliflower"]
choice = random.choice(words)

ans = []
for _ in choice:
    ans.append("__")
print(" ".join(map(str, ans)))

lives = 6
correct = 0
while lives > 0:
    guess = input("\nguess a letter : ").lower()
    flag = 0
    i = 0
    for letter in choice:
        if letter == guess:
            ans[i] = guess
            correct += 1
            flag = 1
        i += 1
    print(" ".join(map(str, ans)))

    if flag == 1:
        print("\nyou guessed it right!!")
        if correct == len(choice):
            print("CONGRATULATIONS !! YOU WIN !")
            exit(0)
    else:
        lives -= 1
        print(f"\nyou guessed wrong!! you have {lives} lives\u2764\uFE0F remaining")

print("OH NO !! YOUR LIVES CAME TO AN END . YOU LOST!")