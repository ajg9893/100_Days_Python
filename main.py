import art
import os

def Auction():
    print(art.logo)

    # Variable set to True if there are more bidders and false if there aren't
    Continue = True

    Bidder_List = {}

    # While loop to keep asking the name and bid amount unless more bidders == 'no'
    while Continue == True:
        name = input("What is your name? ")
        bid = float(input("What would you like to bid? The minimum bid is 30 dollars. "))

        while bid < 30:
            print("Please enter a valid bid. ")
            bid = float(input("What would you like to bid? The minimum bid is 30 dollars. "))

        # Adds the name and bid to a dictionary as a key:value pair
        Bidder_List[name] = bid

        more_bidders = input("Are there any other bidders? ").lower()

        # If there are no more bidders, loop should end and result will display
        if more_bidders == "no":
            Continue = False
            break
        print("*"*40)

    print()
    print("*" * 40)
    # Creates a value for max bid and bidder who holds it
    max_bid = 0
    bidder = ""
    # Loops through the dictionary to check if a bidder has a greater bid than max_bid
    for key in Bidder_List:
        if Bidder_List[key] > max_bid:
            max_bid = Bidder_List[key]
            bidder = key

    print(f"The max bid is held by {bidder} and is ${max_bid}")

Auction()