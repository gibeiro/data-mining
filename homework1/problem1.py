import random
import sys

class Card:
	def __init__(self, suit, symbol):
        	self.suit = suit
        	self.symbol = symbol

suits = ['C','D','H','S']
symbols = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
deck = []

for suit in suits:
	for symbol in symbols:
		card = Card(suit, symbol)
		deck.append(card)

total_samples = int(sys.argv[1])

prob = 'P(The first two cards include at least one ace) = '
favorable_samples = 0.0
for x in range(total_samples):
	random.shuffle(deck)
	for y in range(2):
		if deck[y].symbol == 'A':
			favorable_samples += 1
			break
print prob + str(favorable_samples/total_samples)

prob = 'P(The first five cards include at least one ace) = '
favorable_samples = 0.0
for x in range(total_samples):
	random.shuffle(deck)
	for y in range(5):
		if deck[y].symbol == 'A':
			favorable_samples += 1
			break
print prob + str(favorable_samples/total_samples)

prob = 'P(The first two cards are a pair of the same rank) = '
favorable_samples = 0.0
for x in range(total_samples):
	random.shuffle(deck)
	if deck[0].symbol == deck[1].symbol:
		favorable_samples += 1
print prob + str(favorable_samples/total_samples)

prob = 'P(The first five cards are all diamonds) = '
favorable_samples = 0.0
for x in range(total_samples):
	random.shuffle(deck)
	for y in range(6):
		if y == 5:
			favorable_samples += 1
		elif deck[y].suit != 'D':
			break		
print prob + str(favorable_samples/total_samples)

prob = 'P(The first five cards form a full house) = '
favorable_samples = 0.0
for x in range(total_samples):
	random.shuffle(deck)
	occurrences = []
	for y in range(5):
		occurrences.append(deck[y].symbol)
	occurrences.sort()
	symbol1 = occurrences[0]
	symbol2 = occurrences[4]
	if occurrences.count(symbol1) == 2 and occurrences.count(symbol2) == 3 or occurrences.count(symbol1) == 3 and occurrences.count(symbol2) == 2:
		favorable_samples += 1
print prob + str(favorable_samples/total_samples)
