# TODO-1: Ask the user for input
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
# TODO-2: Save data into dictionary {name: price}
def highest_bid(bids):
    winner = ""
    highest_bid = 0
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

# TODO-3: Whether if new bids need to be added
bids = {}
bidders = True
while bidders:
    user_name = (input("What is your name?: "))
    bid_value = int(input("What is your bid?: $"))
    bids[user_name] = bid_value
    more_players = input("Do you have more bidders? Type 'yes' or 'no': \n ").lower()
    if more_players == 'no':
        bidders = False
        highest_bid(bids)
    elif more_players == 'yes':
        print("\n"* 100 )



# TODO-4: Compare bids in dictionary


