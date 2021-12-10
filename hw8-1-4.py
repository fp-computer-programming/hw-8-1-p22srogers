# Author: SMR (AMDG) 12/10/21
card_one = input("How much is your first card worth?: ")
card_two = input("How much is your second card worth?: ")
def safe_card(card1,card2):
    card_value = int(card1) + int(card2)
    if card_value < 21:
        safe = "You are safe!"
    else:
        print("You are not safe.")
    return safe
print(safe_card(card_one,card_two))