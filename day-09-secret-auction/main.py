# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art

bids = {}
should_continue = True

print(art.logo)

while should_continue:
    new_name = input("Write your name: ")
    new_bid = int(input("Enter your bid: "))

    bids[new_name] = new_bid

    more_bids = input("Are there any other bidders? yes or no: ")
    if more_bids == "no":
        should_continue = False


highest_bidder = ""
highest_bid = 0

for name in bids:
    if bids[name] > highest_bid:
        highest_bidder = name
        highest_bid = bids[name]

print(f"The highest bid was made by {highest_bidder} for a total of {highest_bid}.")
