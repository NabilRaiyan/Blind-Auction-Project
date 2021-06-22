from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo

print(logo)


def bidder_info():
    blind_auction = {}

    next_bidder = True
    while next_bidder:
        bidder_name = input("What is your name?\n")
        biding_amount = int(input("What is your bid?\n$"))

        blind_auction[bidder_name] = biding_amount
        another_bidder = input("Are there any other bidder? Tape 'yes' or 'no'.\n")

        clear()
        if another_bidder == "no":
            next_bidder = False

    def find_highest_bidder():

        highest_bid = 0
        winner = ""
        for bidder in blind_auction:
            bidder_amount = blind_auction[bidder]
            if bidder_amount > highest_bid:
                highest_bid = bidder_amount
                winner = bidder

        print(f"Winner is {winner}, with the bid of  {highest_bid}")

    find_highest_bidder()


bidder_info()
