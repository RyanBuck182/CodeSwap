# BLACKJACK!!!! In python.... sorry I'm not very creative
"""
In Blackjack, the goal is to beat the dealer's hand by getting as close to 21 as possible without exceeding it, with face cards counting as 10 and Aces as 1 or 11.
Here's a breakdown of the super basic rules:

  Objective:
  Players aim to beat the dealer's hand by getting a higher total without exceeding 21.

Card Values:

  Number cards (2-9) have their face value.

Face cards (Jack, Queen, King) and 10s count as 10.
Aces can be 1 or 11, whichever is advantageous to the player.

Gameplay:

  Players place bets, then receive two cards face up, while the dealer receives two cards, one face up and one face down.

Players can "hit" (take more cards) or "stand" (keep their current hand).
If a player's hand exceeds 21, they "bust" and lose.
If the dealer busts, all remaining players win.
If neither busts, the player with the higher hand wins.

Blackjack (21):
A hand of 21 on the first two cards is a "blackjack"
Dealer's Turn:
After players have played their hands, the dealer reveals their face-down card and plays their hand according to the rules, typically hitting until they reach 17 or more.
Push:
If the player and dealer have the same hand total, it's a "push" and the bet is returned.

"""
import random


def create_deck(): # -> a deck!!!
  suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
  ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
  deck = [(rank, suit) for suit in suits for rank in ranks]
  return deck


# a hand is a list of cards
# a card is a tuple of (rank, suit)
def deal(hand, deck) -> None: # -> returns nothing just populates the hand passed in!
  card1 = deck[random.randint(1, len(deck))-1]
  deck.remove(card1)
  hand.append(card1)

  card2 = deck[random.randint(1, len(deck))-1]
  deck.remove(card2)
  hand.append(card2)

def calc_score(hand) -> int:
  score = 0
  has_ace = False

  for card in hand:
    if card[0].isnumeric():
      score += int(card[0])
      continue

    if card[0] =="Jack" or card[0] =="Queen" or card[0] =="King":
      score += 10
      continue

    # if we are still here it means we found an ace!
    has_ace = True

  # if the ace being worth 11 results in a bust then we are gonna make it worth 1
  if has_ace:
    if score + 11 > 21:
      score += 1
    else:
      score += 11

  return score


def hit(hand, deck) -> None:
  card = deck[random.randint(1, len(deck))-1]
  deck.remove(card)
  hand.append(card)


## still need to implement game loop!!!
while True:

  deck = create_deck()

  player_hand = []
  dealer_hand = []

  deal(player_hand, deck)
  deal(dealer_hand, deck)

  # Let the player hit
  while True:
    print(player_hand)
    print("Current Score", calc_score(player_hand))
    choice = input("Do you want to hit? (y/n): ")
    if choice.lower() == 'y':
      hit(player_hand, deck)
    else:
      break

    if calc_score(player_hand) >= 21:
      break

    player_score = calc_score(player_hand)
  
  # Check if player busted
  if calc_score(player_hand) > 21:
    print(f"Your hand: {player_hand}")
    print(f"Your score: {calc_score(player_hand)}")
    print("Bust! You lose!")
    break

  # Dealer's turn
  print("\nDealer's turn:")
  while calc_score(dealer_hand) < 17:
    print(f"Dealer's hand: {dealer_hand}")
    hit(dealer_hand, deck)
  
  dealer_score = calc_score(dealer_hand)
  
  # Show final hands
  print(f"\nYour final hand: {player_hand}")
  print(f"Your final score: {player_score}")
  print(f"Dealer's final hand: {dealer_hand}")
  print(f"Dealer's final score: {dealer_score}")
  
  # Determine winner
  if dealer_score > 21:
    print("Dealer busts! You win!")
  elif player_score > dealer_score:
    print("You win!")
  elif dealer_score > player_score:
    print("Dealer wins!")
  else:
    print("It's a tie!")

  play_again = input("\nPlay again? (y/n): ")
  if play_again.lower() != 'y':
    break


  # print(f'Players Cards: {player_hand}')

  # player_score = calc_score(player_hand)

  # print(player_score)

  break
