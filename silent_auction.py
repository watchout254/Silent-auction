#daniel mukenya nyongs
import sys
data = {}


print(f"*******Welcome to Mukenya's  Silent Auction program*****")
jina = input("What is your name? ")
bid = int(input("What is your bid? "))
data = [jina] = bid
again = input("Are there any bidders? Yes or No..: ").lower()
if again == "yes":

elif again == "no":
    winner()
    sys.exit()

