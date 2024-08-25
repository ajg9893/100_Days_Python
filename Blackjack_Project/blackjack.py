import random
import os
import art

# Dictionary filled with the value of each card
card_value = {
    "Ace": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,

}

# List containing 52 cards to resemble a full deck
cards_list = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"] * 4
random.shuffle(cards_list)

random_num = 0

# Declare the sum of the computer and player's cards
# Create the computer and player's hands
computer_hand = []
player_hand = []
computer_total = 0
player_total = 0


# Gets a random card from the cards_list and gives it hand from the parameter
def get_cards(cards, hand):
    random_num = random.randint(0, len(cards) - 1)
    hand.append(cards[random_num])
    cards.remove(cards[random_num])


def sum_cards(hand):
    total = 0
    for i in range(len(hand)):
        total += card_value[hand[i]]
    return total


# Function for checking if the hand won or is a bust
def check_winner_bust(total1):
    if total1 >= 21:
        return True


def computer(computer_hand, hidden_card, computer_total, cards_list):
    computer_hand.remove("Hidden")
    computer_hand.append(hidden_card)
    print(f"Computer hand: {computer_hand}")

    # Computer is dealt cards until total is greater than or equal to 17
    while computer_total <= 17:
        get_cards(cards_list, computer_hand)
        computer_total = sum_cards(computer_hand)
    print(f"Computer hand: {computer_hand}")
    print(f"Computer's total card values: {computer_total}")



def blackjack():
    print(art.logo)

    # Calls the function to add the cards to the computer and player hands
    get_cards(cards_list, computer_hand)
    get_cards(cards_list, computer_hand)
    get_cards(cards_list, player_hand)
    get_cards(cards_list, player_hand)

    # Sums the value of the player's cards
    player_total = sum_cards(player_hand)
    computer_total = sum_cards(computer_hand)

    # Hides the computer's second card from the user
    hidden_card = computer_hand[1]
    computer_hand.remove(computer_hand[1])
    computer_hand.append("Hidden")

    print(f"Your hand: {player_hand}")
    print(f"Computer hand: {computer_hand}")

    print(f"Your total card values: {player_total}")
    print()

    if (player_total == 21):
        if (computer_total == 21):
            print("\n" * 2)
            print(f"Computer hand: {computer_hand}")
            print(f"Computer's total card values: {computer_total}")
            print("Its a draw... You both have a blackjack!")
            return
        print("Congrats! You have a blackjack!")
        return

    # While loop to ask if the Player wants to hit (get a card)
    while True:

        if input("Would you like to hit? (y/n)  ") == "y":
            get_cards(cards_list, player_hand)
            player_total = sum_cards(player_hand)

            print(f"Your hand: {player_hand}")
            print(f"Computer hand: {computer_hand}")
            print(f"Your total card values: {player_total}")
            print()

            # Checks if the player has yet won
            if check_winner_bust(player_total):
                if player_total > 21:
                    print("It was a bust! You exceeded 21!")
                    return
                else:
                    computer(computer_hand, hidden_card, computer_total, cards_list)
                    if check_winner_bust(computer_total):
                        if (computer_total > 21):
                            print("The computer busted; it exceeded 21! You won!")
                            return
                    break

        else:
            computer(computer_hand, hidden_card, computer_total, cards_list)
            if check_winner_bust(computer_total):
                if (computer_total > 21):
                    print("The computer busted; it exceeded 21! You won!")
                    return
            break

        print("\n" * 4)
        print(f"Your hand: {player_hand}")
        print(f"Computer hand: {computer_hand}")
        print(f"Your total card values: {player_total}")
        print(f"Computer's total card values: {computer_total}")
    # End of outer While Loop

    if player_total == 21:
        if computer_total == 21:
            print("It was a draw! Both the computer and the player reached 21!")
        else:
            print("You reached 21! Congrats you won!!!!! ")
    if computer_total == 21:
        print("The computer reached 21 first! You lose!!!!!")
    if player_total > computer_total:
        print("The player wins! You have a higher score!")
    elif player_total < computer_total:
        print("The computer wins! You have a lower score!")
    else:
        print("You draw! You have equal scores!")


blackjack()
"""if input("Do you want to play a game of Blackjack? (y/n)   ") == "yes":
    blackjack()"""
