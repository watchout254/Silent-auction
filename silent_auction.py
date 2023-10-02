#daniel mukenya nyongs
import sys
import os

def winner(details):
    highest = 0
    mshindi = ""
    for bet in details:
        price = details[bet]
        if price > highest:
            highest=price
            mshindi = bet
    print(f"List of all bidders: {details}")
    print(f"The winner is {mshindi}, with a bid price of {highest}")


data = {}
end_bid  = False
while not end_bid:
    print(f"*******Welcome to Mukenya's  Silent Auction program*****")
    jina = input("What is your name? ")
    bid = int(input("What is your bid? "))
    data[jina] = bid
    again = input("Are there any bidders? Yes or No..: ").lower()
    if again == "no":
        end_bid = True
        winner(data)

    elif again == "yes":
        os.system('cls')


