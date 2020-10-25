import random

def setCards():
	all_cards = []

	suits = [u'\u2764', u'\u2666', u'\u2663', u'\u2660']
	values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

	for suit in suits:
 		for value in values:
			 all_cards.append(value + " " + suit)
	return all_cards

all_cards = setCards()

card_values = {}
	
for card in all_cards:
	if "A" in card:
		card_values[card] = 14
	elif "J" in card:
		card_values[card] = 11
	elif "Q" in card:
		card_values[card] = 12
	elif "K" in card:
		card_values[card] = 13	
	else:
		card_values[card] = int(card[:2])

botDeck = []
playerDeck = []

def playerCards():
  return playerDeck

def botCards():
  return botDeck

def resetCards(_botDeck,_playerDeck):
	_botDeck.clear()
	_playerDeck.clear()

	game_deck = setCards()
	random.shuffle(game_deck)
	_botDeck += game_deck[:len(game_deck)//2]
	_playerDeck += game_deck[len(game_deck)//2:]

	return (f'```New game initiated, WELCOME TO NO MORE ALIVE```')


def war(_botCard, _playerCard):
	if not (checkDecks(botDeck, playerDeck)):
		if (len(botDeck) <= 3):
			declareWinner("Player")
		else:
			declareWinner("Bot")
			
	playerSac1 = playerDeck.pop()
	playerSac2 = playerDeck.pop()
	playerSac3 = playerDeck.pop()
	
	botSac1 = botDeck.pop()
	botSac2 = botDeck.pop()
	botSac3 = botDeck.pop()

	botSacrifice = [botSac1, botSac2, botSac3]
	playerSacrifice = [playerSac1, playerSac2, playerSac3]
	
	botCard = botDeck.pop()
	playerCard = playerDeck.pop()
	
	table = [botCard, playerCard]
	
	turn1 = (f'```You drew: {_playerCard}\nBot drew: {_botCard}```\n')
	
	sacrificed = (f'```You sacrificed: {playerSac1},{playerSac2},{playerSac3}\n Bot sacrificed: {botSac1},{botSac2},{botSac3}```')
  
	turn2 = (f'```You drew: {playerCard}\nBot drew: {botCard}```\n')
  
	
	if(card_values[table[0]] > card_values[table[1]]):
		botDeck.insert(0,botCard)
		botDeck.insert(1,playerCard)
		botDeck.insert(0,botSacrifice)
		botDeck.insert(0,playerSacrifice)

		verdict = (f'```You lost the battle```')
		return turn1 + sacrificed + turn2 + verdict

	
	elif(card_values[table[0]] < card_values[table[1]]):
		playerDeck.insert(0,playerCard)
		playerDeck.insert(1,botCard)
		playerDeck.insert(0,botSacrifice)
		playerDeck.insert(0,playerSacrifice)

		verdict = (f'```You won the battle!```')
		return turn1 + sacrificed + turn2 + verdict	
	else:
		return war(botCard, playerCard)
	


  
def checkDecks(deck1, deck2):
	if(len(deck1) >= 3) and (len(deck2) >= 3):
		return True
	else:
		return False

	
def flip():
	if not (checkDecks(botDeck, playerDeck)):
		if (len(botDeck) <= 3):
			declareWinner("Player")
		else:
			declareWinner("Bot")
	botCard = botDeck.pop()
	playerCard = playerDeck.pop()
		
	table = [botCard, playerCard]
		
	if(card_values[table[0]] > card_values[table[1]]):
		botDeck.insert(0,botCard)
		botDeck.insert(1,playerCard)
		turn = (f'```You drew: {playerCard}\nBot drew: {botCard}```\n')
		return turn + check()
		
	elif(card_values[table[0]] < card_values[table[1]]):
		playerDeck.insert(0,playerCard)
		playerDeck.insert(1,botCard)
		turn = (f'```You drew: {playerCard}\nBot drew: {botCard}```\n')
		return turn + check()
		
	else:
		return war(botCard, playerCard)
		
	

def check():
  return (f'```Player\'s remaining cards: {len(playerDeck)}\nBot\'s remaining cards: {len(botDeck)}```')

def declareWinner(player):
  return (f'```This player won: {player}!```')


	
	
	
	



'''def start_game(botDeck, playerDeck):'''