from colorama import init
import random
from Ricks_Casino_Loan_Office import Ricks_Casino_Loan_Office as Ricks_CLO



class Three_Card_Poker():
	def __init__(self,PlayerCash,PlayerDebt):
		init()
		self.Card_Deck = ['HA','H2','H3','H4','H5','H6','H7','H8','H9','HJ','HQ','HK','DA','D2','D3','D4','D5','D6','D7','D8','D9','DJ','DQ','DK','CA','C2','C3','C4','C5','C6','C7','C8','C9','CJ','CQ','CK','SA','S2','S3','S4','S5','S6','S7','S8','S9','SJ','SQ','SK']
		self.Shuffle_Deck()
		self.PlayerCash = PlayerCash
		self.PlayerDebt = PlayerDebt
		self.AnteBet = 0
		self.Round2Bet = 0
		self.PairPlusBet = 0
		self.HasPairPlus = False
		self.HasAnte = False
		self.CutCard = 6
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

	def Sort_Hand(self,Hand):
		card0 = Hand[0]
		card1 = Hand[1]
		card2 = Hand[2]
		fval0 = list(card0)
		fval0 = fval0[1]
		fval1 = list(card1)
		fval1 = fval1[1]
		fval2 = list(card2)
		fval2 = fval2[1]
		if fval0 == 'J':
			fval0=10
		elif fval0 == 'Q':
			fval0=11
		elif fval0 == 'K':
			fval0=12
		elif fval0 == 'A':
			fval0=13
		if fval1 == 'J':
			fval1=10
		elif fval1 == 'Q':
			fval1=11
		elif fval1 == 'K':
			fval1=12
		elif fval1 == 'A':
			fval1=13
		if fval2 == 'J':
			fval2=10
		elif fval2 == 'Q':
			fval2=11
		elif fval2 == 'K':
			fval2=12
		elif fval2 == 'A':
			fval2=13
		if int(fval0) > int(fval1) and int(fval0) > int(fval2):
			if int(fval1) > int(fval2):
				Hand = [card2,card1,card0]
			elif int(fval1) < int(fval2):
				Hand = [card1,card2,card0]
			elif int(fval1) == int(fval2):
				Hand = [card1,card2,card0]
		elif int(fval1) > int(fval0) and int(fval1) > int(fval2):
			if int(fval0) > int(fval2):
				Hand = [card2,card0,card1]
			elif int(fval0) < int(fval2):
				Hand = [card0,card2,card1]
			elif int(fval0) == int(fval2):
				Hand = [card0,card2,card1]
		elif int(fval2) > int(fval0) and int(fval2) > int(fval1):
			if int(fval0) > int(fval1):
				Hand = [card1,card0,card2]
			elif int(fval0) < int(fval1):
				Hand = [card0,card1,card2]
			elif int(fval0) == int(fval1):
				Hand = [card1,card0,card2]
		return Hand

	def Print_Board(self, P_Hand,D_Hand,ShowDealer):
		print '\033[2J'
		x = 0
		y = 0
		P_Hand = self.Sort_Hand(P_Hand)
		D_Hand = self.Sort_Hand(D_Hand)
		for card in P_Hand:
			self.Print_Card(card,x,y)
			x += 1
			y += 6
		x = 12
		y = 0
		ccount = 0
		for card in D_Hand:
			if ShowDealer == False:
				self.Print_Card('XX',x,y)
			else:
				self.Print_Card(card,x,y)
			x += 1
			y += 6
			ccount += 1
		self.Print_Stats(24,3)

	def Print_Stats(self,x,y):
		print '{3}\033[{0};{1}HPlayer Cash: {2}{4}'.format(x,y,self.PlayerCash,self.GREEN,self.NO_COLOUR)
		print '{3}\033[{0};{1}HAnte Bet: {2}{4}'.format(x+1,y,self.AnteBet,self.GREEN,self.NO_COLOUR)
		print '{3}\033[{0};{1}HPlay Bet: {2}{4}'.format(x+2,y,self.Round2Bet,self.GREEN,self.NO_COLOUR)
		print '{3}\033[{0};{1}HPairPlus Bet: {2}{4}'.format(x+3,y,self.PairPlusBet,self.GREEN,self.NO_COLOUR)

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
{12}\033[{4};{3}H{14}|{13}{12} {1}   {1} {14}|
{12}\033[{5};{3}H{14}|{13}{12}  {0} {0}  {14}|
{12}\033[{6};{3}H{14}|{13}{12}       {14}|
{12}\033[{7};{3}H{14}|{13}{12}    {0}  {14}|
{12}\033[{8};{3}H{14}|{13}{12}       {14}|
{12}\033[{9};{3}H{14}|{13}{12}  {0} {0}  {14}|
{12}\033[{10};{3}H{14}|{13}{12} {1}   {1} {14}|
{12}\033[{11};{3}H{14}----------'''.format(FValue,SValue,x,y,x+1,x+2,x+3,x+4,x+5,x+6,x+7,x+8,c_color,self.BLUEBKGD,self.BLACKBKGD)
		print Pretty_Card

	def Bet_Bank(self, AddorSub, T_Value):
		if AddorSub == 'Add':
			self.PlayerCash += T_Value
		if AddorSub == 'Sub':
			self.PlayerCash -= T_Value
		if AddorSub == 'Bal':
			print '{1}Your Current Balance is : {2}{0}{3}'.format(self.PlayerCash,self.BLUE,self.GREEN,self.NO_COLOUR)

	def Take_Bet_Ante(self):
		if self.PlayerCash == 0:
			return
		bet_placed = False
		print 'Player Account Balance:'
		self.Bet_Bank('Bal',0)

		while bet_placed != True:
			validbet = None
			while validbet != True:
				try:
					yourbet = input('{0}How Much Would you like to bet on Ante? : {1}'.format(self.BLUE,self.NO_COLOUR))
					validbet = True
				except:
					print '{0}Thats not a valid bet{1}'.format(self.RED,self.NO_COLOUR)
					validbet = False
					yourbet = 0
					continue

			if yourbet <= self.PlayerCash:
				self.Bet_Bank('Sub', yourbet)
				self.AnteBet = yourbet
				self.HasAnte = True
				yourbet = 0
				bet_placed = True
			else:
				print '{0}You cannot afford to make this bet.{1}'.format(self.RED,self.NO_COLOUR)
				yourbet = 0
				bet_placed = False

	def Take_Bet_Round_2(self):
		if self.PlayerCash == 0:
			return
		print 'Player Account Balance:'
		self.Bet_Bank('Bal',0)

		bet_placed = False
		while bet_placed != True:
			validbet = None
			while validbet != True:
				try:
					print('{0}Let\'s see those cards. Doubling Ante! : {1}'.format(self.BLUE,self.NO_COLOUR))
					validbet = True
				except:
					print '{0}Thats not a valid bet{1}'.format(self.RED,self.NO_COLOUR)
					validbet = False
					yourbet = 0
					continue

			if self.AnteBet <= self.PlayerCash:
				self.Bet_Bank('Sub', self.AnteBet)
				self.Round2Bet = self.AnteBet
				bet_placed = True
			else:
				print '{0}You cannot afford to make this bet.{1}'.format(self.RED,self.NO_COLOUR)
				yourbet = 0
				return False
	def Take_Bet_PairPlus(self):
		if self.PlayerCash == 0:
			return
		print 'Player Account Balance:'
		self.Bet_Bank('Bal',0)
		bet_placed = False
		while bet_placed != True:
			validbet = None
			while validbet != True:
				try:
					yourbet = input('{0}How Much Would you like to bet on PairPlus? : {1}'.format(self.BLUE,self.NO_COLOUR))
					validbet = True
				except:
					print '{0}Thats not a valid bet{1}'.format(self.RED,self.NO_COLOUR)
					validbet = False
					yourbet = 0
					continue

			if yourbet <= self.PlayerCash:
				self.Bet_Bank('Sub', yourbet)
				self.PairPlusBet = yourbet
				self.HasPairPlus = True
				yourbet = 0
				bet_placed = True
			else:
				print '{0}You cannot afford to make this bet.{1}'.format(self.RED,self.NO_COLOUR)
				yourbet = 0
				bet_placed = False
	def Pay_Bets(self,isbj):
		if isbj == 'ABH':
			Winnings = self.AnteBet + self.Round2Bet
			self.Bet_Bank('Add', Winnings)
			self.Bet_Bank('Add', (self.AnteBet + self.Round2Bet))
			print 'You won {0} for your bet of {1}'.format(Winnings,(self.AnteBet + self.Round2Bet))
		if isbj == 'ANQ':
			Winnings = self.AnteBet
			self.Bet_Bank('Add', Winnings)
			self.Bet_Bank('Add', (self.AnteBet ))
			print 'You won {0} for your bet of {1}'.format(Winnings,(self.AnteBet))
		elif isbj == 'ASF':
			Winnings = (self.AnteBet + self.Round2Bet)  * 9
			self.Bet_Bank('Add', Winnings)
			self.Bet_Bank('Add', (self.AnteBet + self.Round2Bet))
			print 'You won {0} for your bet of {1}'.format(Winnings,(self.AnteBet + self.Round2Bet))


		elif isbj == 'ATOK':
			Winnings = (self.AnteBet + self.Round2Bet)  * 8
			self.Bet_Bank('Add', Winnings)
			self.Bet_Bank('Add', (self.AnteBet + self.Round2Bet))
			print 'You won {0} for your bet of {1}'.format(Winnings,(self.AnteBet + self.Round2Bet))

		elif isbj == 'AS':
			Winnings = (self.AnteBet + self.Round2Bet)
			self.Bet_Bank('Add', Winnings)
			self.Bet_Bank('Add', (self.AnteBet + self.Round2Bet))
			print 'You won {0} for your bet of {1}'.format(Winnings,(self.AnteBet + self.Round2Bet))

		if isbj == 'PPSF':
			Winnings = (self.PairPlusBet) * 40
			self.Bet_Bank('Add', Winnings)
			self.Bet_Bank('Add', (self.PairPlusBet))
			print 'You won {0} for your bet of {1}'.format(Winnings,(self.PairPlusBet))

		elif isbj == 'PPTOK':
			Winnings = (self.PairPlusBet) * 32
			self.Bet_Bank('Add', Winnings)
			self.Bet_Bank('Add', (self.PairPlusBet))
			print 'You won {0} for your bet of {1}'.format(Winnings,(self.PairPlusBet))

		elif isbj == 'PPF':
			Winnings = (self.PairPlusBet) * 4
			self.Bet_Bank('Add', Winnings)
			self.Bet_Bank('Add', (self.PairPlusBet))
			print 'You won {0} for your bet of {1}'.format(Winnings,(self.PairPlusBet))

		elif isbj == 'PPP':
			Winnings = (self.PairPlusBet)
			self.Bet_Bank('Add', Winnings)
			self.Bet_Bank('Add', (self.PairPlusBet))
			print 'You won {0} for your bet of {1}'.format(Winnings,(self.PairPlusBet))


		elif isbj == 'PPS':
			Winnings = (self.PairPlusBet) * 6
			self.Bet_Bank('Add', Winnings)
			self.Bet_Bank('Add', (self.PairPlusBet))
			print 'You won {0} for your bet of {1}'.format(Winnings,(self.PairPlusBet))

		if isbj == 'ClearAllBets':
			self.AnteBet = 0
			self.Round2Bet = 0
			self.HasAnte = False
			self.PairPlusBet = 0
			self.HasPairPlus = False

	def New_Deck(self):
		if len(self.Card_Deck) < self.CutCard:
			print 'Out of cards, Shuffling New Deck!'
			self.Card_Deck = ['HA','H2','H3','H4','H5','H6','H7','H8','H9','HJ','HQ','HK','DA','D2','D3','D4','D5','D6','D7','D8','D9','DJ','DQ','DK','CA','C2','C3','C4','C5','C6','C7','C8','C9','CJ','CQ','CK','SA','S2','S3','S4','S5','S6','S7','S8','S9','SJ','SQ','SK']
			self.Shuffle_Deck()
			self.CutCard = 6

	def Shuffle_Deck(self):
		random.shuffle(self.Card_Deck)
		random.shuffle(self.Card_Deck)
		random.shuffle(self.Card_Deck)

	def Deal_Card(self):
		card = self.Card_Deck.pop(0)
		#print card
		return card

	def Deal_Hand(self):
		P_Hand = []
		D_Hand = []
		ccount = 0
		while ccount < 3:
			P_Hand.append(self.Deal_Card())
			D_Hand.append(self.Deal_Card())
			ccount += 1
		self.Print_Board(P_Hand,D_Hand,False)
		return P_Hand,	D_Hand

	def Eval_Hand_R2(self,P_Hand,D_Hand):

		p_card0 = list(P_Hand[0])
		p_card1 = list(P_Hand[1])
		p_card2 = list(P_Hand[2])

		d_card0 = list(D_Hand[0])
		d_card1 = list(D_Hand[1])
		d_card2 = list(D_Hand[2])

		P_Hand_Rank,P_High_Card = self.Rank_Hand(P_Hand,False)
		D_Hand_Rank,D_High_Card = self.Rank_Hand(D_Hand,True)
		self.Print_Board(P_Hand,D_Hand,True)
		if D_Hand < 6 or D_High_Card > 10:
			if P_Hand_Rank < D_Hand_Rank:
				print '{0}Your Hand Beat the Dealer, Paying even money.{1}'.format(self.GREEN,self.NO_COLOUR)
				self.Pay_Bets('ABH')
			elif P_Hand_Rank > D_Hand_Rank:
				print '{0}The Dealer Beat your Hand. {2}Checking for other Wins.{1}'.format(self.RED,self.NO_COLOUR,self.GREEN)
			elif P_Hand_Rank == D_Hand_Rank:
				if P_High_Card > D_High_Card:
					print '{0}Your Hand Beat the Dealer, Paying even money.{1}'.format	(self.GREEN,self.NO_COLOUR)
					self.Pay_Bets('ABH')
				elif P_High_Card < D_High_Card:
					print '{0}The Dealer Beat your Hand. {2}Checking for other Wins.{1}'.format(self.RED,self.NO_COLOUR,self.GREEN)
				else:
					print '{0}It\'s a push. Returning Ante/Round2 bets, {2}Checking for other Wins.{1}'.format(self.BLUE,self.NO_COLOUR,self.GREEN)
		else:
			print '{0}The Dealer didn\'t qualify. Paying even money on Ante, {2}Forfit R2 Bet.{1}'.format(self.GREEN,self.NO_COLOUR,self.RED)
			self.Pay_Bets('ANQ')

	def Eval_Hand_R1(self,P_Hand,D_Hand):

		p_card0 = list(P_Hand[0])
		p_card1 = list(P_Hand[1])
		p_card2 = list(P_Hand[2])

		d_card0 = list(D_Hand[0])
		d_card1 = list(D_Hand[1])
		d_card2 = list(D_Hand[2])

		P_Hand_Rank,P_High_Card = self.Rank_Hand(P_Hand,False)
		D_Hand_Rank,P_High_Card = self.Rank_Hand(D_Hand,True)
		if self.HasAnte == True:
			if P_Hand_Rank <= 3:
				print '{2}Checking for other Wins.{1}'.format(self.BLUE,self.NO_COLOUR,self.GREEN)
				if P_Hand_Rank == 1:
					print '{0}Paying on Straight Flush!{1}'.format	(self.GREEN,self.NO_COLOUR)
					self.Pay_Bets('ASF')
				elif P_Hand_Rank == 2:
					print '{0}Paying on Three of a Kind!{1}'.format	(self.GREEN,self.NO_COLOUR)
					self.Pay_Bets('ATOK')

				elif P_Hand_Rank == 3:
					print '{0}Paying on Straight!{1}'.format	(self.GREEN,self.NO_COLOUR)
					self.Pay_Bets('AS')
		if self.HasPairPlus == True:
			print '{0}Paying on PairPlus Bets!{1}'.format	(self.GREEN,self.NO_COLOUR)
			if P_Hand_Rank == 1:
				print '{0}Paying on Straight Flush!{1}'.format	(self.GREEN,self.NO_COLOUR)
				self.Pay_Bets('PPSF')

			elif P_Hand_Rank == 2:
				print '{0}Paying on Three of a Kind!{1}'.format	(self.GREEN,self.NO_COLOUR)
				self.Pay_Bets('PPTOK')

			elif P_Hand_Rank == 3:
				print '{0}Paying on Straight!{1}'.format	(self.GREEN,self.NO_COLOUR)
				self.Pay_Bets('PPS')

			elif P_Hand_Rank == 4:
				print '{0}Paying on Flush!{1}'.format	(self.GREEN,self.NO_COLOUR)
				self.Pay_Bets('PPF')

			elif P_Hand_Rank == 5:
				print '{0}Paying on Pair!{1}'.format	(self.GREEN,self.NO_COLOUR)
				self.Pay_Bets('PPP')

	def Rank_Hand(self,Hand,Dealer):
		card0 = list(Hand[0])
		card1 = list(Hand[1])
		card2 = list(Hand[2])
		if card0[1] == 'J':
			card0[1]=10
		elif card0[1] == 'Q':
			card0[1]=11
		elif card0[1] == 'K':
			card0[1]=12
		elif card0[1] == 'A':
			card0[1]=13
		if card1[1] == 'J':
			card1[1]=10
		elif card1[1] == 'Q':
			card1[1]=11
		elif card1[1] == 'K':
			card1[1]=12
		elif card1[1] == 'A':
			card1[1]=13
		if card2[1] == 'J':
			card2[1]=10
		elif card2[1] == 'Q':
			card2[1]=11
		elif card2[1] == 'K':
			card2[1]=12
		elif card2[1] == 'A':
			card2[1]=13

		c_list = [int(card0[1]),int(card1[1]),int(card2[1])]
		c_list.sort()
		#print c_list
		if card0[0] == card1[0]	and card0[0] == card2[0]:
			if c_list[0] == c_list[1] - 1 and c_list[0] == c_list[2] - 2:
				if Dealer == False:
					print '{2}You have a {0}Straight Flush!{1}'.format(self.RED,self.NO_COLOUR,self.GREEN)
				return 1, c_list[2]
			else:
				if Dealer == False:
					print '{2}You have a {0}Flush!{1}'.format(self.RED,self.NO_COLOUR,self.GREEN)
				return 4,c_list[2]

		elif card0[1] == card1[1] and card0[1] == card2[1]:
			if Dealer == False:
				print '{2}You have a {0}Three of a Kind!{1}'.format(self.RED,self.NO_COLOUR,self.GREEN)
			return 2,c_list[2]

		elif c_list[0] == c_list[1] - 1 and c_list[0] == c_list[2] - 2:
			if Dealer == False:
				print '{2}You have a {0}Straight!{1}'.format(self.RED,self.NO_COLOUR,self.GREEN)
			return 3,c_list[2]

		elif card0[1] == card1[1]:
			if Dealer == False:
				print '{2}You have a {0}Pair!{1}'.format(self.RED,self.NO_COLOUR,self.GREEN)
			return 5,c_list[0]

		elif card0[1] == card2[1]:
			if Dealer == False:
				print '{2}You have a {0}Pair!{1}'.format(self.RED,self.NO_COLOUR,self.GREEN)
			return 5,c_list[0]

		elif card1[1] == card2[1]:
			if Dealer == False:
				print '{2}You have a {0}Pair!{1}'.format(self.RED,self.NO_COLOUR,self.GREEN)
			return 5,c_list[2]

		else:
			if Dealer == False:
				print '{2}You have a {0}High Card!{1}'.format(self.RED,self.NO_COLOUR,self.GREEN)
			return 6,c_list[2]

	def Play_TCP(self):
		another_hand = 'a'

		print '{2}Welcome to {0}Pickle Ricks{1} {3}Three Card Poker Game{1}'.format(self.GREEN,self.NO_COLOUR,self.BLUE,self.LIGHT_RED)
		while another_hand.upper() != 'Q':
			self.New_Deck()
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
			self.Pay_Bets('ClearAllBets')
			another_hand = raw_input('{0} Try your luck again? Y/N/Q{1}'.format(self.BLUE,self.NO_COLOUR))
			if another_hand.upper() == 'Y':
				print
			elif another_hand.upper() == 'N':
				return self.PlayerCash,self.PlayerDebt
			Bet_Ante = raw_input('{0} Would you like to Ante? Y/N{1}'.format(self.GREEN,self.NO_COLOUR))
			if Bet_Ante.upper() == 'Y':
				self.Take_Bet_Ante()
			else:
				print ('OK, But you got to bet to win.{1}'.format(self.BLUE,self.NO_COLOUR))
			Bet_PP = raw_input('{0} Would you like bet Pair Plus? Y/N{1}'.format(self.GREEN,self.NO_COLOUR))
			if Bet_PP.upper() == 'Y':
				self.Take_Bet_PairPlus()
			else:
				print ('OK, But you got to bet to win.{1}'.format(self.BLUE,self.NO_COLOUR))
			if Bet_PP.upper() != 'Y' and Bet_Ante.upper() != 'Y':
				print ('{0}You have to make a bet to play!{1}'.format(self.LIGHT_RED,self.NO_COLOUR))
			else:
				P_Hand,D_Hand = self.Deal_Hand()
				self.Eval_Hand_R1(P_Hand,D_Hand)
				Bet_R2 = raw_input('{0} Would you like bet for Round 2? Y/N{1}'.format(self.GREEN,self.NO_COLOUR))
				if Bet_R2.upper() == 'Y':
					self.Take_Bet_Round_2()
					self.Eval_Hand_R2(P_Hand,D_Hand)
				else:
					print ('{0}OK, Let move to the next hand. {1}'.format(self.BLUE,self.NO_COLOUR))
					continue
		return PlayerCash, PlayerDebt
