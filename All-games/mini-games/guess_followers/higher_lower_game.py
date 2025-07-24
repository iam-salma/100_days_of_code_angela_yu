import random
import hl_data


def check_ans(ch, i, j):
    global score
    if guess == 'A' and i["follower_count"] > j["follower_count"]:
        score += 1
        print(f"Your right ! current score = {score}")
        return True
    elif guess == 'B' and i["follower_count"] < j["follower_count"]:
        score += 1
        print(f"Your right ! current score = {score}")
        return True
    else:
        print(f"oh no! You were wrong! final score = {score}")
        return False


score = 0
while True:
    x = random.choice(hl_data.data)
    y = random.choice(hl_data.data)
    print("Compare A: ", end="")
    print(f"{x["name"]} , {x["description"]} , {x["country"]}.")
    print("\nAgainst B: ", end="")
    print(f"{y["name"]} , {y["description"]} , {y["country"]}.")

    guess = input("who has more followers? Type 'A' or 'B' : ").upper()
    if not check_ans(guess, x, y):
        break
