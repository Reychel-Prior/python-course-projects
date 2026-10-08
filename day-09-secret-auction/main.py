# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

bids = {}
should_continue = True

while should_continue:
    new_name = input("Write your name: ")
    new_bid = input("Enter your bid: ")

    bids[new_name] = new_bid

    more_bids = input("Are there any other bidders? yes or no: ")
    if more_bids == "no":
        should_continue = False
