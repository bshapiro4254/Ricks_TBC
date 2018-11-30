from colorama import init
import random
from Ricks_Casino_Loan_Office import Ricks_Casino_Loan_Office as Ricks_CLO

class Black_Jack():
	def __init__(self,PlayerCash,PlayerDebt):
		init()
		self.DeckSize = None
		self.Card_Deck = []
		while self.DeckSize == None:
			try:
				self.DeckSize = input('How Many Decks do you want to play? 2 or 6 :')
			except:
				print 'You Must Enter a Number 2 or 6!'
				self.DeckSize = None
				continue
			if self.DeckSize == 6 or self.DeckSize == 2:
				continue
			else:
				print 'You Must Enter a Number 2 or 6!'
				self.DeckSize = None
				continue
		D_Count = 1
		Card_Deck = ['HA','H2','H3','H4','H5','H6','H7','H8','H9','HJ','HQ','HK','DA','D2','D3','D4','D5','D6','D7','D8','D9','DJ','DQ','DK','CA','C2','C3','C4','C5','C6','C7','C8','C9','CJ','CQ','CK','SA','S2','S3','S4','S5','S6','S7','S8','S9','SJ','SQ','SK']
		while self.DeckSize >= D_Count:
				for card in Card_Deck:
					self.Card_Deck.append(card)
				D_Count += 1
		if self.DeckSize == 2:
			self.CutCard = random.randint(38,58)
		if self.DeckSize == 6:
			self.CutCard = random.randint(52,78)
		self.Shuffle_Deck()
		self.PlayerCash = PlayerCash
		self.PlayerDebt = PlayerDebt
		self.CurrentBet = 0
		self.DoubleBet = 0
		self.DoubleBet2 = 0
		self.InsuranceBet = 0
		self.HasInsurance = False
		self.HasDouble = False
		self.IsSplit = False
		self.BLUE="\033[1;36m"
		self.RED="\033[1;31m"
		self.LIGHT_RED="\033[1;31m"
		self.WHITE="\033[1;37m"
		self.GREEN="\033[1;32m"
		self.GREY="\033[1;30m"
		self.BLACK="\033[0;30m"
		self.BLUEBKGD ="\033[0;44m"
		self.GREENBKGD ="\033[0;42m"
		self.GREYBKGD ="\033[0;47m"
		self.WHITEBKGD ="\033[0;39m"
		self.BLACKBKGD ="\033[0;40m"
		self.NO_COLOUR="\033[0m"
		self.CPalete=[self.WHITEBKGD,self.BLACKBKGD,self.BLUEBKGD,self.GREENBKGD,self.GREYBKGD,self.WHITE,self.BLACK,self.GREY,self.RED,self.LIGHT_RED,self.GREEN,self.BLUE,self.NO_COLOUR]
	def Return_PCash(self):
		return self.PlayerCash

	def Return_PDebt(self):
		return self.PlayerDebt

	def Print_Board(self, P_Hand,D_Hand,ShowDealer):
		print '\033[2J'
		x = 0
		y = 0
		for card in P_Hand:
			self.Print_Card(card,x,y)
			x += 1
			y += 6
		x = 12
		y = 0
		ccount = 0
		for card in D_Hand:
			if ccount == 0 and ShowDealer == False:
				self.Print_Card('XX',x,y)
			else:
				self.Print_Card(card,x,y)
			x += 1
			y += 6
			ccount += 1
		self.Print_Stats(24,3)

	def Print_Split(self, P_Hand_1,P_Hand_2,D_Hand,ShowDealer):
		print '\033[2J'
		x = 0
		y = 0
		for card in P_Hand_1:
			self.Print_Card(card,x,y)
			x += 1
			y += 6
		x = 0
		y = 40
		for card in P_Hand_2:
			self.Print_Card(card,x,y)
			x += 1
			y += 6
		x = 12
		y = 0
		ccount = 0
		for card in D_Hand:
			if ccount == 0 and ShowDealer == False:
				self.Print_Card('XX',x,y)
			else:
				self.Print_Card(card,x,y)
			x += 1
			y += 6
			ccount += 1
		self.Print_Stats(24,3)

	def Print_Stats(self,x,y):
		print '{3}\033[{0};{1}HPlayer Cash: {2}{4}'.format(x,y,self.PlayerCash,self.GREEN,self.NO_COLOUR)
		print '{3}\033[{0};{1}HCurrent Bet: {2}{4}'.format(x+1,y,self.CurrentBet,self.GREEN,self.NO_COLOUR)
		print '{3}\033[{0};{1}HInsurance Bet: {2}{4}'.format(x+2,y,self.InsuranceBet,self.GREEN,self.NO_COLOUR)
		print '{3}\033[{0};{1}HDoubleDown Bet: {2}{4}'.format(x+3,y,self.DoubleBet,self.GREEN,self.NO_COLOUR)
		print '{3}\033[{0};{1}HDoubleDown Bet 2: {2}{4}'.format(x+4,y,self.DoubleBet2,self.GREEN,self.NO_COLOUR)

	def Print_Card(self,Card,x,y):
		Card = list(Card)
		FValue = Card[1]
		SValue = Card[0]
		Heart = u'\u2665'
		Diamond = u'\u25C6'
		Spade = u'\u2660'
		Club = u'\u2663'
		if SValue in ['H', 'D']:
			c_color = self.RED
			if SValue == 'H':
				suit = Heart
			if SValue == 'D':
				suit = Diamond
		elif SValue in ['S', 'C']:
			c_color = self.BLUE
			if SValue == 'S':
				suit = Spade
			if SValue == 'C':
				suit = Club
		elif SValue == 'X':
			c_color = self.WHITE
		Pretty_Card = '''{12}\033[{2};{3}H{14}--------
\033[{4};{3}H{14}|{13}{12} {1}   {1} {14}|
\033[{5};{3}H{14}|{13}{12}  {0} {0}  {14}|
\033[{6};{3}H{14}|{13}{12}       {14}|
\033[{7};{3}H{14}|{13}{12}    {0}  {14}|
\033[{8};{3}H{14}|{13}{12}       {14}|
\033[{9};{3}H{14}|{13}{12}  {0} {0}  {14}|
\033[{10};{3}H{14}|{13}{12} {1}   {1} {14}|
\033[{11};{3}H{14}----------'''.format(FValue,SValue,x,y,x+1,x+2,x+3,x+4,x+5,x+6,x+7,x+8,c_color,self.BLUEBKGD,self.BLACKBKGD)
		print Pretty_Card

	def Bet_Bank(self, AddorSub, T_Value):
		if AddorSub == 'Add':
			self.PlayerCash += T_Value
		if AddorSub == 'Sub':
			self.PlayerCash -= T_Value
		if AddorSub == 'Bal':
			print '{1}Your Current Balance is : {2}{0}{3}'.format(self.PlayerCash,self.BLUE,self.GREEN,self.NO_COLOUR)

	def Take_Bet(self):
		print 'Player Account Balance:'
		self.Bet_Bank('Bal',0)

		bet_placed = False
		while bet_placed != True:
			validbet = None
			while validbet != True:
				try:
					yourbet = input('{0}How Much Would you like to bet? : {1}'.format(self.BLUE,self.NO_COLOUR))
					validbet = True
				except:
					print '{0}Thats not a valid bet{1}'.format(self.RED,self.NO_COLOUR)
					validbet = False
					yourbet = 0
					continue

			if yourbet <= self.PlayerCash:
				self.Bet_Bank('Sub', yourbet)
				self.CurrentBet = yourbet
				yourbet = 0
				bet_placed = True
			else:
				print '{0}You cannot afford to make this bet.{1}'.format(self.RED,self.NO_COLOUR)
				yourbet = 0
				bet_placed = False

	def Hit_Menu(self,x,y,P_Hand,D_Hand):
		isI  = self.Check_Insurance(D_Hand)
		isSP = self.Check_Split(P_Hand)
		D = 'Double Down : DD'
		S = 'Stand       : SD'
		SP ='Split       : SP'
		H = 'Hit         :  H'
		E = 'Enter Selection:'

		l1 ='\033[{1};{0}H'.format(y,x,x+1,x+2,x+3,x+4,x+5,x+6,x+7,x+8,x+9,x+10)
		l2='\033[{2};{0}H'.format(y,x,x+1,x+2,x+3,x+4,x+5,x+6,x+7,x+8,x+9,x+10)
		l3='\033[{3};{0}H'.format(y,x,x+1,x+2,x+3,x+4,x+5,x+6,x+7,x+8,x+9,x+10)
		l4='\033[{4};{0}H'.format(y,x,x+1,x+2,x+3,x+4,x+5,x+6,x+7,x+8,x+9,x+10)
		l5='\033[{5};{0}H'.format(y,x,x+1,x+2,x+3,x+4,x+5,x+6,x+7,x+8,x+9,x+10)
		l6='\033[{6};{0}H'.format(y,x,x+1,x+2,x+3,x+4,x+5,x+6,x+7,x+8,x+9,x+10)
		l7='\033[{7};{0}H'.format(y,x,x+1,x+2,x+3,x+4,x+5,x+6,x+7,x+8,x+9,x+10)
		l8='\033[{8};{0}H'.format(y,x,x+1,x+2,x+3,x+4,x+5,x+6,x+7,x+8,x+9,x+10)
		l9='\033[{9};{0}H'.format(y,x,x+1,x+2,x+3,x+4,x+5,x+6,x+7,x+8,x+9,x+10)
		l10='\033[{10};{0}H'.format(y,x,x+1,x+2,x+3,x+4,x+5,x+6,x+7,x+8,x+9,x+10)
		options = ['H','SD','DD']
		if isI == True:
			 options.append('I')
		if isSP == True:
			options.append('SP')


		if isI == False:
			I = '                '
		elif isI == True:
			I = 'Insurance   :  I'
		if isSP == False:
			SP = '                '
		elif isSP == True:
			SP = 'Split       : SP'

		menu = '''{5}{16}____________________{20}
{6}{17}|{16}{19} {0} {17}|{20}
{7}{17}|{16}{19} {1} {17}|{20}
{8}{17}|{16}{19} {2} {17}|{20}
{9}{17}|{16}{19} {3} {17}|{20}
{10}{17}|{16}{19} {15} {17}|{20}
{11}{17}|__________________|{20}
{12}{17}|{16}{19} {4} {17}|{20}
{13}{17}|__________________|{20}'''.format(D,S,H,I,E,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,SP,self.GREENBKGD,self.BLACKBKGD,self.BLACK,self.BLUE,self.NO_COLOUR)
		HS = None
		while HS == None:
			print menu
			#try:
			HS = raw_input()
			HS = HS.upper()
			if HS.upper() in options:
				if HS == 'H':
					return HS,HS

				elif HS == 'SD':
					return HS,HS

				elif HS == 'SP':
					self.Offer_Split(P_Hand)
					return HS,returncode

				elif HS == 'DD':
					returncode = self.Offer_Double(P_Hand)
					if returncode == True:
						self.Play_Double(P_Hand,D_Hand)
					else:
						print
					return HS,HS

				elif HS == 'I' and isI == True:
					returncode = self.Offer_Isurance(D_Hand)
					return HS,returncode
			else:
				print '{13}That is not a valid selection. Please Try Again.'.format(D,S,H,I,E,l1,l2,l3,l4,l5,l6,l7,l8,l9)
				raw_input()
				self.Print_Board(P_Hand,D_Hand,False)
				print menu

				HS = None
				continue
			#except:
				#print '{13}That is not a valid selection. Please Try Again.'.format(D,S,H,I,E,l1,l2,l3,l4,l5,l6,l7,l8,l9)
				#raw_input()
				#self.Print_Board(P_Hand,D_Hand,False)
				#print menu

				#HS = None
				#continue

	def Offer_Double(self,P_Hand):
		betplaced = None
		if self.PlayerCash == 0:
			return
		print 'Player Account Balance:'
		self.Bet_Bank('Bal',0)

		if self.Eval_Hand(P_Hand)  > 12:
			card = P_Hand[1]
			card = list(card)
			card = card[1]
			card0 = P_Hand[0]
			card0 = list(card0)
			card0 = card0[1]
			#if card0 != 'A' and card != 'A':
				#return


#		pdd = raw_input('{0}Want to Double Down? Y/N: {1}'.format(self.BLUE,self.NO_COLOUR))
		#		if pdd.upper() == 'Y':
		while betplaced != True:
			validbet = None
			while validbet != True:
				try:
					self.DoubleBet = input('Enter your bet to Max {0} : '.format(self.CurrentBet))
					validbet = True
				except:
					print 'Thats not a valid bet'
					validbet = False
					self.DoubleBet = 0
					continue


			if self.DoubleBet <= self.CurrentBet:
				if self.DoubleBet <= self.PlayerCash:
					self.Bet_Bank('Sub',self.DoubleBet)
					self.HasDouble = True
					betplaced = True
					return True
				else:
					print 'You do not have that ammount to bet!'
					self.DoubleBet = 0
					betplaced = False
					return True
			else:
				print 'That exceeds the max bet!'
				self.DoubleBet = 0
				betplaced = False
#		if pdd.upper == 'N':
#			print 'OK, Good luck!'
#			return False

	def Check_Insurance(self,D_Hand):
		card = D_Hand[1]
		card = '{0}'.format(card)
		card = list(card)
		card0 = D_Hand[0]
		card0 = '{0}'.format(card0)
		card0 = list(card0)
		#print card
		if card[1] == 'A':
			return True
		else:
			return False

	def Offer_Isurance(self,D_Hand):
		if self.PlayerCash == 0:
			return
		card = D_Hand[1]
		card = '{0}'.format(card)
		card = list(card)
		card0 = D_Hand[0]
		card0 = '{0}'.format(card0)
		card0 = list(card0)
		#print card
		if card[1] == 'A':
			print 'Dealer is showing an Ace!'
#			ins = raw_input('{0}Do you want to buy insurance? Y/N:{1}'.format(self.BLUE,self.NO_COLOUR))
#			if ins.upper() == 'Y':
			betplaced = False
			while betplaced != True:
				self.Bet_Bank('Bal',0)
				validbet = None
				while validbet != True:
					try:
						ins_bet = input('How much will you bet?')
						if float(ins_bet) >= (self.CurrentBet / 2) and ins_bet <= self.PlayerCash:
							validbet = True
							break
						else:
							print 'Thats not a valid bet. Must be > {0}'.format(self.CurrentBet / 2)
							validbet = False
							ins_bet = 0
							continue

					except:
						print 'Thats not a valid bet'
						validbet = False
						ins_bet = 0
						continue

				if ins_bet <= self.PlayerCash:
					print 'Thank you for your bet, Good Luck!'
					self.HasInsurance = True
					self.Bet_Bank('Sub',ins_bet)
					self.InsuranceBet = ins_bet
					betplaced = True
				else:
					print 'You dont have that amount to bet'
					betplaced = False
					ins_bet = 0
					continue
			if card0 in ['K','Q','J']:
				print 'Dealer Has BlackJack, Paying Insurance'
				self.Pay_Bets('I')
				return True
			else:
				print 'Dealer Doesn\'t have BlackJack, Insurance Forfit'
				return False

		elif self.Is_BlackJack(D_Hand) == True:
			print 'Dealer has BlackJack, You didnt buy insurance. Sorry.'
			self.Pay_Bets('L')
			return True

#			else:
#				print 'Ok, Best of Luck.'
#				return False

	def Check_Split(self,P_Hand):
		card1 = P_Hand[0]
		card1 = list(card1)
		card1 = card1[1]
		card2 = P_Hand[1]
		card2 = list(card2)
		card2 = card2[1]
		if card1 == card2:
			return True
		else:
			return False

	def Offer_Split(self,P_Hand):

		if self.PlayerCash == 0:
			return
		card1 = P_Hand[0]
		card1 = list(card1)
		card1 = card1[1]
		card2 = P_Hand[1]
		card2 = list(card2)
		card2 = card2[1]
		if card1 == card2:
			print 'You have a pair!'
#			splitit = raw_input('{0}Would you like to split it? Y/N: {1}'.format(self.BLUE,self.NO_COLOUR))
#			if splitit.upper() == 'Y':
			if self.CurrentBet <= self.PlayerCash:
				print 'Splitting...'
				self.Bet_Bank('Sub',self.CurrentBet)
				self.IsSplit = True
				return True
			else:
				print 'You do not have that ammount to bet!'
				return False
		else:
			print 'Ok, Best of Luck.'
			return False


	def Pay_Bets(self,isbj):
		if isbj == 'Y':
			Winnings = self.CurrentBet * 1.5
			self.Bet_Bank('Add', Winnings)
			self.Bet_Bank('Add', self.CurrentBet)
			print 'You won {0} for your bet of {1}'.format(Winnings,self.CurrentBet)
		elif isbj == 'N':
			Winnings = self.CurrentBet
			self.Bet_Bank('Add', Winnings)
			self.Bet_Bank('Add', self.CurrentBet)
			print 'You won {0} for your bet of {1}'.format(Winnings,self.CurrentBet)
			if self.HasDouble == True:
				DWinnings = self.DoubleBet
				self.Bet_Bank('Add', DWinnings)
				self.Bet_Bank('Add', self.DoubleBet)
				print 'You won {0} for your double bet of {1}'.format(DWinnings,self.DoubleBet)

		elif isbj == 'L':
			print

		elif isbj == 'P':
			Winnings = self.CurrentBet
			self.Bet_Bank('Add', Winnings)

		elif isbj == 'I':
			Winnings = self.CurrentBet + (self.CurrentBet * 2)
			self.Bet_Bank('Add', Winnings)
			self.Bet_Bank('Add', self.InsuranceBet)
			print 'You won {0} for your insurance bet of {1}'.format(Winnings,self.CurrentBet)

		self.DoubleBet = 0
		self.CurrentBet = 0
		self.InsuranceBet = 0
		self.HasInsurance = False
		self.HasDouble = False

	def New_Deck(self):
		if len(self.Card_Deck) < self.CutCard:
			print 'Out of cards, Shuffling New Deck!'
			D_Count = 1
			Card_Deck = ['HA','H2','H3','H4','H5','H6','H7','H8','H9','HJ','HQ','HK','DA','D2','D3','D4','D5','D6','D7','D8','D9','DJ','DQ','DK','CA','C2','C3','C4','C5','C6','C7','C8','C9','CJ','CQ','CK','SA','S2','S3','S4','S5','S6','S7','S8','S9','SJ','SQ','SK']
			while self.DeckSize >= D_Count:
					for card in Card_Deck:
						self.Card_Deck.append(card)
			if self.DeckSize == 2:
				self.CutCard = random.randint(38,58)
			if self.DeckSize == 6:
				self.CutCard = random.randint(52,78)
			self.Shuffle_Deck()
			self.CutCard = random.randint(38,58)

	def Shuffle_Deck(self):
		random.shuffle(self.Card_Deck)
		random.shuffle(self.Card_Deck)
		random.shuffle(self.Card_Deck)

	def Deal_Card(self):
		card = self.Card_Deck.pop(0)
		#print card
		return card

	def Deal_Hand(self):
		D_Count = 0
		Ao9 = random.randint(0,1)
		if Ao9 == 0:
			My_Hand = ['A']
		if Ao9 == 1:
			My_Hand = [9]
		C_Count = random.randint(2,4)
		while D_Count != C_Count:
			My_Hand.append(Deal_Card())
			D_Count += 1
		return My_Hand

	def Eval_Hand(self,My_Hand):
		H_Sum = 0
		A_Present = 0
		#print My_Hand
		for card in My_Hand:
			if type(card) != str:
				continue
			#print card
			card = '{0}'.format(card)
			card = list(card)
			#print card
			if card[1] == 'A':
				A_Present = A_Present + 1
				H_Sum = H_Sum + 11
			elif card[1] in [ 'J', 'Q', 'K' ]:
				H_Sum = H_Sum + 10
			else:
				H_Sum = H_Sum + int(card[1])
		if A_Present >= 1:
			if H_Sum > 21:
				H_Sum = H_Sum - 10
				if H_Sum > 21 and A_Present >=2:
					H_Sum = H_Sum - 10
					if H_Sum > 21 and A_Present >=3:
						H_Sum = H_Sum - 10
						if H_Sum > 21 and A_Present >=4:
							H_Sum = H_Sum - 10
							if H_Sum > 21 and A_Present >=5:
								H_Sum = H_Sum - 10
								if H_Sum > 21 and A_Present >=6:
									H_Sum = H_Sum - 10
									if H_Sum > 21 and A_Present >=7:
										H_Sum = H_Sum - 10
										if H_Sum > 21 and A_Present >=8:
											H_Sum = H_Sum - 10
		return H_Sum

	def Is_BlackJack(self,hand):
		card1 = list(hand[0])
		card2 = list(hand[1])

		if card1[1] == 'A':
			if card2[1] in ['J','Q','K']:
				return True
		elif card2[1] == 'A':
			if card1[1] in ['J','Q','K']:
				return True
		else:
			return False

	def Eval_And_Pay(self,P_Hand,D_Hand, round):
		if round == 1:
			if self.Is_BlackJack(P_Hand) == True:
				if self.Is_BlackJack(D_Hand) == True:
					print 'Sorry pal, thats a push.'
					self.Pay_Bets('P')
					if self.HasInsurance == True:
						self.Pay_Bets('I')
						return True
				else:
					print 'You Won the Hand.'
					self.Pay_Bets('Y')
					return True
			else:
				return False
		elif round == 2:
			if self.Eval_Hand(P_Hand) > 21:
				print 'You Bust! Sorry Pal!'

			elif self.Is_BlackJack(D_Hand) == True:
				print 'Dealer has Black Jack.'
				if self.HasInsurance == True:
					self.Pay_Bets('I')
				if self.Eval_Hand(P_Hand) == 21:
					print 'You have 21, it\'s a push'
					self.Pay_Bets('P')

			elif self.Eval_Hand(D_Hand) > 21:
				print 'Dealer Busts. You Win!!!'
				self.Pay_Bets('N')

			elif self.Eval_Hand(P_Hand) == 21:
				print 'You Have 21, The Hard Way.'
				self.Pay_Bets('N')

			elif self.Eval_Hand(P_Hand) > self.Eval_Hand(D_Hand):
				print 'Your Hand Beat the Dealers. You Win!!!'
				self.Pay_Bets('N')

			elif self.Eval_Hand(P_Hand) < self.Eval_Hand(D_Hand):
				print 'Your Hand Lost to the Dealers. Better Luck Next Time!!!'
				self.Pay_Bets('L')

			elif self.Eval_Hand(P_Hand) == self.Eval_Hand(D_Hand):
				print 'Your Hand Matched the Dealers. You Push!!!'
				self.Pay_Bets('P')

	def Play_Double(self,P_Hand,D_Hand):
		print 'Dealing One Card...'
		P_Hand.append(self.Deal_Card())

		self.Print_Board(P_Hand,D_Hand,True)
		while self.Eval_Hand(D_Hand) <= 16:
			D_Hand.append(self.Deal_Card())
		self.Print_Board(P_Hand,D_Hand,True)
		print 'Paying Winning Bets for Hand 1.'
		self.Eval_And_Pay(P_Hand,D_Hand,2)
		return D_Hand

	def Split_Cards(self,P_Hand,D_Hand):
		P_Hand_1 = [P_Hand[0]]

		P_Hand_2 = [P_Hand[1]]

		card1 = P_Hand[0]
		card1 = list(card1)
		card1 = card1[1]
		if card1 == 'A':

			print 'Dealing cards...'
			P_Hand_1.append(self.Deal_Card())
			P_Hand_2.append(self.Deal_Card())
			self.Print_Split(P_Hand_1,P_Hand_2,D_Hand)
		else:


			print 'Dealing cards for hand 1...'
			h1c = 0
			offerdouble1 = None
			while self.Eval_Hand(P_Hand_1) < 21 and anothercard !='D':
				anothercard = self.Hit_Menu(20,35,P_Hand,D_Hand)(P_Hand,D_Hand)
				h1c += 1

				if anothercard.upper() in ['I','D','SD','SP']:
					break
				else:
					continue
			h2c = 0
			offerdouble2 = None
			while self.Eval_Hand(P_Hand_2) < 21 and anothercard !='D':
				print 'Dealing cards for hand 2...'
				anothercard = self.Hit_Menu(20,35,P_Hand,D_Hand)(P_Hand,D_Hand_2)
				if anothercard.upper() == 'N':
					break
				h2c += 1
				if anothercard2.upper() in ['I','D','SD','SP']:
						break
				else:
					continue
		return



	def Play_BJ(self):
		another_hand = 'a'
		self.New_Deck()
		print '{2}Welcome to {0}Pickle Ricks{1} {3}Black Jack Game{1}'.format(self.GREEN,self.NO_COLOUR,self.BLUE,self.LIGHT_RED)
		while another_hand.upper() != 'Q':
			if self.PlayerCash == 0:
				loan_accepted = None
				print '''{0}You reach into your pockets for another bet, but find nothing.
{1}Sweat Drips from your forehead as you notice the Pit Boss talking to security and motioning in your direction.
{2}Time to make a break for it. As you run out the doors Pickle Rick's Casino Loan officer stops you {3}and offers you a loan.{4}'''.format(self.BLUE,self.LIGHT_RED,self.RED,self.GREEN,self.NO_COLOUR)
				try:
					pause=raw_input('Press Any Key')
					RCLO = Ricks_CLO(self.PlayerCash,self.PlayerDebt)
					self.PlayerCash,self.PlayerDebt = RCLO.Menu()
				except:
					RCLO = Ricks_CLO(self.PlayerCash,self.PlayerDebt)
					self.PlayerCash,self.PlayerDebt = RCLO.Menu()

			D_Hand = []
			P_Hand = []
			self.New_Deck()
			print 'Player Account Balance:'
			self.Bet_Bank('Bal',0)
			self.Take_Bet()
			print 'Dealing cards...'
			n = 0
			while n < 2:
				P_Hand.append(self.Deal_Card())
				D_Hand.append(self.Deal_Card())
				n += 1
			#print 'Your hand : {0}'.format(P_Hand)
			#print 'Dealer has : [ X , {0} ]'.format(D_Hand[1])
			self.Print_Board(P_Hand,D_Hand,False)
			(H_Result, H_Sub_Result) = self.Hit_Menu(20,35,P_Hand,D_Hand)
			if H_Result == 'I':
				if H_Sub_Result == True:
					another_hand = raw_input('{0} Try your luck again? Y/N/Q{1}'.format(self.BLUE,self.NO_COLOUR))
					if another_hand.upper() == 'Y':
						continue
					elif another_hand.upper() == 'N':
						return (self.Return_PCash(),self.Return_PDebt())

			if self.Is_BlackJack(D_Hand) == True:
				print 'Dealer Has BlackJack. Better Luck Next Time!!!'
				self.Pay_Bets('L')
				if another_hand.upper() == 'Y':
					continue
				elif another_hand.upper() == 'N':
					return (self.Return_PCash(),self.Return_PDebt())
			Menu_count = 1
			while self.Eval_Hand(P_Hand) < 21 and H_Result not in ['I','SD','DD','SP']:
				if Menu_count > 0:
					Menu_count +=1
					self.Print_Board(P_Hand,D_Hand,False)
					(H_Result, H_Sub_Result) = self.Hit_Menu(20,35,P_Hand,D_Hand)
				if H_Result == 'SD':
					break

				if H_Result == 'SP':
					self.Split_Cards(P_Hand,D_Hand)
					another_hand = raw_input('{0} Try your luck again? Y/N/Q{1}'.format(self.BLUE,self.NO_COLOUR))
					if another_hand.upper() == 'Y':
						continue
					elif another_hand.upper() == 'N':
						return (self.Return_PCash(),self.Return_PDebt())

				elif H_Result == 'H':
					con_hand = False
					while H_Result == 'H' and 21 > self.Eval_Hand(P_Hand):
						if H_Result.upper() == 'H':
							H_Result = None
							P_Hand.append(self.Deal_Card())
							self.Print_Board(P_Hand,D_Hand,False)
							if 21 < self.Eval_Hand(P_Hand):
								print 'Sorry pal, you busted.'
								self.Pay_Bets('L')
								another_hand = raw_input('{0} Try your luck again? Y/N/Q{1}'.format(self.BLUE,self.NO_COLOUR))
								if another_hand.upper() == 'Y':
									con_hand = True
									break
								elif another_hand.upper() == 'N':
									return (self.Return_PCash(),self.Return_PDebt())
								else:
									con_hand = True
									break
				elif H_Result == 'DD':
					break

			self.Print_Board(P_Hand,D_Hand,True)
			while self.Eval_Hand(D_Hand) <= 16:
					D_Hand.append(self.Deal_Card())
			self.Print_Board(P_Hand,D_Hand,True)
			self.Eval_And_Pay(P_Hand,D_Hand,2)

			another_hand = raw_input('{0} Try your luck again? Y/N/Q{1}'.format(self.BLUE,self.NO_COLOUR))
			if another_hand.upper() == 'Y':
				continue
			elif another_hand.upper() == 'N':
				return (self.Return_PCash(),self.Return_PDebt())
		return (self.Return_PCash(),self.Return_PDebt())
