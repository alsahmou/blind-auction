from replit import clear
import art
print(art.logo)
bids = {}
bidding = True 
while bidding:
  name = input("What is your name?")
  bid = int(input("What\'s your bid?'"))
  bids[name] = bid
  others = input("Are there any other bidders?").lower()
  clear()
  if others == 'no':
    bidding = False
    
max_bid = 0
for key in bids:
  if bids[key] > max_bid:
    max_bid = bids[key]
    max_bidder = key
print(f'The winner is {max_bidder}with a bid of ${max_bid}')