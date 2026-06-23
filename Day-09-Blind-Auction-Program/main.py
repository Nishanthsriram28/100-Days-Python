# 1: Ask the user for input
# 2: Save data into dictionary {name: price}
# 3: Whether if new bids need to be added
# 4: Compare bids in dictionary

import art
print(art.logo)
other_bidders = True
auction_dictionary = {}
prize = 0
bidder_name = ""
while other_bidders == True:
    name = input("What is your name ?")
    bid_price = int(input("What is the Bid Price $ :"))
    if bid_price > prize:
        prize = bid_price
        bidder_name = name
    auction_dictionary[name]=bid_price
    any_others = str(input("Any other Biddders ?? yes or no"))
    if any_others == "yes":
        print("\n" * 100)
        other_bidders = True
    elif any_others == "no":
        other_bidders = False

print(f"The winner is {bidder_name} with a bid of ${prize}")















