'''
Janardhan's Blackjack program
'''
from random import randint

## Global constants
value = {'A':11, 'K':10, 'J': 10, 'Q':10,
	         '2':2, '3':3, '4':4, '5':5,
	         '6':6, '7':7, '8':8, '9':9,
	         '10':10}

class CardDeck():
	'''
	Class for deck of cards
	'''
	def __init__(self):
		face = ['A', 'K', 'J', 'Q', '2', '3', '4', '5', '6', '7', '8', '9', '10']
		# Create lists of tuples for each suit
		# eg. spades = [('A', '♠'), ('K', '♠'),...,('10', '♠') ]
		spades = list(zip(face, ['♠']*13))
		clubs = list(zip(face, ['♣']*13))
		diamonds = list(zip(face, ['♦']*13))
		hearts = list(zip(face, ['♥']*13))
		# concatenate all suits to form the deck
		self.deck = []
		self.deck = self.deck + spades + clubs + diamonds + hearts
	
	
	def deal(self):
		cardnumber = randint(0, len(self.deck)-1) # index of a random card
		return(self.deck.pop(cardnumber))

class Player():
	'''
	Contains variables and methods related to player
	'''
	def __init__(self, name, bankroll=1000):
		self.name = name
		self.bankroll = bankroll
		self.hand = [] # list of cards player is holding
		self.score = 0 # sum of cards player holds i.e. score
		self.wins = 0
		self.busts = 0
		self.losses = 0
		self.draws = 0
		self.blackjacks =0
	def bet(self, betplaced):
		self.betplaced = betplaced
		self.bankroll-=self.betplaced
	def hit(self, card):
		self.hand.append(card)
		self.score = 0
		for i in range(0,len(self.hand)):
			self.score += value[self.hand[i][0]] # refer to the global variable value for the card value
		if(self.score>21): #if player goes over 21, check for any Aces that can be counted as 1
			for i in range(0,len(self.hand)):
				if(self.hand[i][0] == 'A' and self.score>21):
					self.score-=10 # give advantage of taking Ace to 1 if player busts
					break

def display_table(player, dealer):
	print('\n'*100)
	print("Player Bankroll = ${}".format(player.bankroll))
	print("Player bet = ${}".format(player.betplaced))
	print('Dealer: {}, Score: {}'.format(dealer.hand, dealer.score))
	print('Player: {}, Score: {}'.format(player.hand, player.score))

def display_table_dealer_hidden(player, dealer):
	print('\n'*100)
	print("Player Bankroll = ${}".format(player.bankroll))
	print("Player bet = ${}".format(player.betplaced))
	print('Dealer: {}   X'.format(dealer.hand[0], dealer.score))
	print('Player: {}, Score: {}'.format(player.hand, player.score))

def display_welcome(player):
	print('\n'*100)
	print('Welcome to BlackJack!!')
	print("{}'s Bankroll = ${}".format(player.name, player.bankroll))
	print("Blackjacks: {}".format(player.blackjacks))
	print("Busts: {}".format(player.busts))
	print("Wins: {}".format(player.wins))
	print("Losses: {}".format(player.losses))
	print("Draws: {}".format(player.draws))

if __name__=='__main__':

	print('\n'*100)
	print('Welcome to Blackjack, creating new player')
	playername = input('Enter name: ')
	playerbankroll = float(input('Enter bankroll: $'))
	player = Player(playername, playerbankroll)
	dealer = Player("Dealer", 1000000.0)
	mydeck = CardDeck()
	while True: # loop for each game
		
		display_welcome(player)
		if(player.bankroll <= 0):
			print("Sorry! You are out of money, bye bye")
			break

		display_welcome(player)
		continueplaying = input("Press any key to continue (q to quit): ")
		if(continueplaying.lower() == 'q'):
			break
		
		display_welcome(player)
		if len(mydeck.deck) <=10:
			print("Starting a new deck since there are less than 10 cards!")
			mydeck = CardDeck() # Create a new shuffled deck if there are too few cards
		
		# New game starts here

		# Set value of hands to zero initially
		player.score = 0
		dealer.score = 0
		blackjack=0 #flag to track if either player got a blackjack
		player_bust = 0 #whether player has busted in this game
		player.hand = []
		dealer.hand = []

		# Ask for bet from player
		display_welcome(player)
		betplaced = float(input("Enter your bet: "))
		if betplaced <= player.bankroll:
			player.bet(betplaced)
		else:
			print("Sorry your bet exceeds your bankroll, so I'll bet your bankroll!")
			input("Press any key to continue: ")
			betplaced = player.bankroll
			player.bet(betplaced)
		
		# initial deal
	
		player.hit(mydeck.deal())
		dealer.hit(mydeck.deal())
		player.hit(mydeck.deal())
		dealer.hit(mydeck.deal())

		## Display initial cards two up for player, one up, one down for dealer
		display_table_dealer_hidden(player, dealer)

		# Check for player blackjack
		if player.score == 21:
			if dealer.score !=21:
				display_table(player, dealer)
				print("Blackjack to Player!")
				player.blackjacks+=1
				player.bankroll+=2.5*betplaced #gets his bet back plus 1.5x of bet from dealer plus original bet
				blackjack=1
			else:
				display_table(player, dealer)
				print("Draw")
				player.blackjacks+=1
				dealer.blackjacks+=1
				player.bankroll+=betplaced #player gets back his bet
			input("Press any key to continue: ")
			continue #go to next game
		elif dealer.score == 21: #and player did not get blackjack
			display_table(player, dealer)
			print("Blackjack to dealer! You lose")
			dealer.blackjacks+=1
			player.losses+=1
			blackjack=1
			input("Press any key to continue: ")
		else: #neither have got a black jack, player plays then dealer may play
			while True: # Player's turn
				choice = input("Hit (press y to hit)? ")
				choice = choice.lower()
				if choice=='y':
					player.hit(mydeck.deal())
					display_table_dealer_hidden(player, dealer)
					if player.score<21:
						continue
					elif player.score>21:
						display_table(player, dealer)
						print("Player Busts!")
						input("Press any key to continue: ")
						player.busts+=1
						dealer.wins+=1
						player_bust=1
						break
					elif player.score==21:
						break # Player stands by default
				else:
					break

			if player_bust!=1:# Dealer's turn
				while True:
					if dealer.score < 17:
						dealer.hit(mydeck.deal())
						display_table(player, dealer)
						input("Press any key to continue: ")
					elif dealer.score >21:
						display_table(player, dealer)
						print("Dealer Busts! You win!")
						player.bankroll+=2*betplaced
						dealer.busts+=1
						player.wins+=1
						input("Press any key to continue: ")
						break
					else:
						break # Dealer stands

		if(dealer.score<=21 and player.score<=21 and blackjack==0): # i.e. nobody busted
			display_table(player, dealer)
			if(player.score > dealer.score):
				print("Player Wins!")
				player.bankroll+=2*betplaced
				player.wins+=1
				dealer.losses+=1
				input("Press any key to continue: ")
			elif(player.score == dealer.score):
				print("Draw!")
				player.bankroll+=betplaced
				player.draws+=1
				dealer.draws+=1
				input("Press any key to continue: ")
			else:
				print("Dealer Wins!")
				dealer.wins+=1
				player.losses+=1
				input("Press any key to continue: ")



	print("Thank you for playing Blackjack!")










