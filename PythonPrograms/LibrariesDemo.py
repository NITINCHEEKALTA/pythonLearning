from random import choice
from random import randint
from random import shuffle

# chice function returns a random string from list  
coin = choice(["heads", "tails"])
print(coin)

"""==============================================="""
# generating a random number
number = randint(1,10)
print(number)

"""========================================"""

cards = ["king", "Queen", "Jack"]
shuffle(cards)
for card in cards:
    print(card)
