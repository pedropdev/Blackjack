############### Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


from art import logo
import random


def deal_card():
    """Draws a card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a hand and calculate the score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw."
    elif computer_score == 0:
        return "Lose,opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over, You lose"
    elif computer_score > 21:
        return "Opponent went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"


def play_game():
    player_hand = []
    computer_hand = []
    player_score = 0
    computer_score = 0
    print(logo)

    is_game_over = False
    for _ in range(2):
        player_hand.append(deal_card())
        computer_hand.append(deal_card())

    while not is_game_over:
        player_score = calculate_score(player_hand)
        computer_score = calculate_score(computer_hand)
        print(f" Your cards: {player_hand}, current score: {player_score}")
        print(f" Computer's first card: {computer_hand[0]}.")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                player_hand.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)

    print(f"  Your final hand: {player_hand}, final score: {player_score}")
    print(f"  Computer's final hand: {computer_hand}, final score: {computer_score}")
    print(compare(player_score, computer_score))

    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
        play_game()


play_game()
