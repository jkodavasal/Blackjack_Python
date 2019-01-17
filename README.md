# Blackjack_Python
Python Blackjack game created using OOP for Jose Portilla's Python Course on Udemy
Created in Python 3.7.1
>>> print(sys.version)
3.7.1 (default, Dec 14 2018, 13:28:58) 
[Clang 4.0.1 (tags/RELEASE_401/final)]

# Running the program
Run on command line as follows:
$python blackjack.py

# Brief description
The program is fairly simple. I have used Object Oriented Programming. In this version of Blackjack, there is no option for insurance or double down. Also it is a single player versus the dealer (computer). Ace can take a value of 11 or 1 on a player's hand based on what is more advantageous to that player. Same holds for the dealer. Read this Quora post for more details: https://www.quora.com/When-is-an-ace-considered-as-1-or-11-in-Blackjack

For an overview of Blackjack, read https://blog.udemy.com/blackjack-rules-2/

To understand it better, download a Blackjack app on your phone and play for sometime: I used *__Blackjack21: Blackjackist from #1 Blackjack__*, available on the Iphone App store. Note that this game allows multiple players, insurance, and double downs, which are not implemented in my simple version of the game. Just ignore the other players (as their cards or bets don't affect your outcome -- at least for these purposes) and insurance/double down options for now.

# Logic

- Initialize player with a name and amount in bankroll (player is an object of class Player)
- Initialize dealer (as an object of class Player). Note the name and bankroll for the dealer are unused, since we assume the dealer is the computer, and the bankroll is infinte.
- Initialize a deck of cards (as an object mydeck, which contains a list, mydeck.deck, which is a list of tuples, the first element of the tuple being the Name or Number on the card (say A, Q, 10, 2, etc.), and the second element being the suit (which is a symbol representing clubs, spades, etc.)

Go through Steps 1 through 5 (each iteration of Step 1 through 5 represents a single game) until player decides to quit, or he runs out of money from his bank roll

- If the deck has less than or equal to 10 cards left, reinitialize a new deck, otherwise continue with the same deck
- Note "hitting" means dealing a card from the deck and adding it to the player's or dealer's hand as the case may be
- When you deal a card, it is removed from the deck. So mydeck.deck "pops" out this card or tuple using the function "pop"
- hand is an attribute of the objects of class Player, and is basically a list of tuples representing the card the player (or dealer) has. This list is similar in structure to the mydeck.deck list.

## Step 1: Deal the first two cards for player and dealer:


1. Player receives a card face up (picked randomly from the deck)
2. Dealer receives a card face down (picked randomly from the deck)
3. Player receives second card face up (picked randomly from the deck)
4. Dealer receives second card face down, and flips his first card to face up (picked randomly from the deck)

This is implemented in the game in the same order as above, however, it only displays the final outcome, i.e., two face up cards for the player, and one face down (second card) and one face up card (first card) for the dealer.

## Step 2: Check for Blackjacks (4 possible outcomes)

Check if either dealer or player has a blackjack (a total of 21 on the first two cards itself).
1. Player has blackjack, dealer doesn't --> **Player wins the game and gets his bet amount back plus 1.5x his bet amount from the dealer. Game ends**
2. Player has blackjack and dealer also has blackjack --> **Draw (or Push), and player gets back his bet amount only. Game ends**
3. Dealer has blackjack, but player doesn't --> **Dealer wins, and player loses his bet. Game ends**
4. If neither has blackjack, go to Step 3. *__Game continues__*

## Step 3: Player's turn (3 possible outcomes)

If neither has a blackjack (a total of 21 on the first two cards itself as in Step 1), then player can proceed to "hit" i.e. get new cards from the deck until (note this will be a loop until (a), (b), or (c) is satisfied): 
1. his total exceeds 21 (busts, i.e. loses his bet) --> **Dealer wins, and player loses his bet. Game ends**
2. he gets exactly 21 --> Player automatically "stands" or ends his turn and proceed to Step 4 for dealer's turn. *__Game continues__*
3. he decides to "stand".  --> Proceed to Step 4 for dealer's turn. *__Game continues__*

## Step 4: Dealer's turn (2 possible outcomes)

The dealer has no flexibility in how he plays. After the player has finished playing (i.e. reaches 21 or stands -- note to get to this point, neither the dealer nor player had a blackjack in Step 2, and the player did not "bust" in Step 3), then the dealer keeps "hitting" (implemented as a loop) or getting more cards from the deck, until:
1. the dealer "busts"; say for eg. if he has a total hand value of 14 (without an Ace in this example -- see note on Aces at the top), and then proceeds to pick a 9 for example, his total would now be 24, which is > 21, so dealer busts, and player wins. --> **Player wins, and gets his bet money back plus an amount equal to the bet from the dealer. Game ends**
2. dealer ends up with a hand value of anywhere between 17 and 21. Then dealer is obligated to "stand" -- this is a Casino rule. --> Proceed to Step 5. *__Game continues__*

## Step 5: Pick a winner (assuming neither player nor dealer has busted or has a hand value >21, and neither has got a blackjack) (3 possible outcomes)

1. If player's hand's value > dealer's hand's value --> **Player wins, and gets his bet money back plus an amount equal to the bet from the dealer. Game ends**
2. If dealer's hand's value > player's hand value --> **Dealer wins, player loses his bet money. Game ends**
3. Both have same hand value --> **Draw (or Push), and player gets his bet money back. Game ends**

### Note: 
Everytime a player bets, his bankroll is reduced by the amount of the bet. If he wins, he gets his bet money back (to his bankroll), plus winnings (1.5x of bet for Blackjack, and 1.0x of bet otherwise)



