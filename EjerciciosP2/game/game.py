import random

SUITS = "♠ ♣ ♥ ♦".split()
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

def create_deck(shuffle=False):
    deck = [(s,r) for r in RANKS for s in SUITS]    
    if shuffle:
        random.shuffle(deck)
    return deck

def deal_hands(deck):
    return (deck[0:5], deck[5:10])

def play():
    deck = create_deck(shuffle=True)
    names = "CPU Player".split()
    hand = {n:h for n,h in zip(names,deal_hands(deck))}

    for names, cards in hand.items():
        card_str = " ".join(f"{s}{r}" for (s,r) in cards)
        print(f"{names}: {card_str}")

if __name__ == "__main__":
    play()
