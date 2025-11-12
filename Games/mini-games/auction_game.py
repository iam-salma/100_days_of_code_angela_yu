

auction_data = {}
while True:
    name = input("whats your name? : ")
    bid = int(input("whats your bid? : $"))
    auction_data[name] = bid
    check = input("Are there any other bidders? type \"yes\" or \"no\"").lower()
    if check == "no":
        break
    else:
        print("\n" * 100)

maxi = 0
winner = ""
for bidder, bid in auction_data.items():
    if bid > maxi:
        maxi = bid
        winner = bidder
print(f"The winner of this auction is {winner} with a bid of ${maxi}")