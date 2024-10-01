from art import logo

print(logo)


# TODO-4: Compare bids in dictionary
def find_highest_bidding(bidding_dictionary):
    winner=""
    highest_bid=0
    for bidder in bidding_dictionary:
        bid_amount=bidding_dictionary[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")


bids={}
continue_bidding=True
while continue_bidding:
    name = input("What's your name? ")
    price= int(input("What's your bid? $"))
    bids[name]=price
    should_continue=input("Type 'yes' to add more bids or 'no' to stop the auction:").lower()
    if should_continue=="no":
        continue_bidding=False
        find_highest_bidding(bids)
    elif should_continue=="yes":
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")




