# Beat the dealer by having a hand total closer to 21 without going over (busting).
# detect blackjack(ace + 10)
# if comp has blackjack , comp wins even if user has a blackjack
# if user has blackjack and comp does not, user wins
# ace = 11 but if sum>21 then ace = 1
# game ends if user score > 21 or if comp gets blackjack
# the comp will keep drawing cards till score > 16

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_pick = [random.choice(cards), random.choice(cards)]
comp_pick = [random.choice(cards), random.choice(cards)]

user = {
    "score": sum(user_pick),
    "has_black_jack": False
}
comp = {
    "score": sum(comp_pick),
    "has_black_jack": False
}


def draw_card():
    while True:
        choice = input("do you want to pick a card? [y/n]: ").lower()
        if choice == 'n':
            print("your final hand : ", user_pick)
            calculate_score()
            break

        user_pick.append(random.choice(cards))
        print("your final hand : ", user_pick)

    while sum(comp_pick) < 16:
        comp_pick.append(random.choice(cards))
    print("comp's final hand : ", comp_pick)
    calculate_score()


def black_jack():
    if user_pick == [11, 10] or user_pick == [10, 11]:
        user["has_black_jack"] = True
    if comp_pick == [11, 10] or comp_pick == [10, 11]:
        comp["has_black_jack"] = True


def calculate_score():
    black_jack()
    if comp["has_black_jack"] is True:
        comp["score"] = 0
        return
    elif user["has_black_jack"] is True and comp["has_black_jack"] is False:
        user["score"] = 0
        return
    else:
        user["score"] = sum(user_pick)
        comp["score"] = sum(comp_pick)
        ace_value()


def ace_value():
    change = 0
    i = 0
    for card in user_pick:
        if card == 1 and user["score"] < 11:
            user_pick.remove(card)
            user_pick.insert(i, 11)
            change = 1
        if card == 11 and user["score"] > 21:
            user_pick.remove(card)
            user_pick.insert(i, 1)
            change = 1
        i += 1
    j = 0
    for card in comp_pick:
        if card == 1 and comp["score"] < 11:
            comp_pick.remove(card)
            comp_pick.insert(j, 11)
            change = 1
        if card == 11 and comp["score"] > 21:
            comp_pick.remove(card)
            comp_pick.insert(j, 1)
            change = 1
        j += 1
    if change == 1:
        calculate_score()


def result():
    if user["score"] == 0:
        print("you win! you got black jack !")
    elif comp["score"] == 0:
        print("comp wins ! it got a black jack !")
    elif (user["score"] > 21) and comp["score"] > 21:
        print("both lose !")
        return
    elif ((user["score"] > comp["score"]) and user["score"] <= 21) or comp["score"] > 21:
        print("you win !")
    elif ((user["score"] < comp["score"]) and comp["score"] <= 21) or user["score"] > 21:
        print("comp wins !")
    else:
        print("its a draw")


print("your cards : ", user_pick)
print("comp's cards : [", comp_pick[0], ", ? ]")
calculate_score()
draw_card()
print(f"your score = {user["score"]} and computers score = {comp["score"]}")
result()
