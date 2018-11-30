from colorama import init
import random
class Ricks_Casino_Loan_Office():
	def __init__(self,PlayerCash,PlayerDebt):
		init()
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
		self.PlayerCash=PlayerCash
		self.PlayerDebt=PlayerDebt
		self.CurrentRate = random.randint(20,40) * .01

	def Print_Office(self):
		x = 5
		y = 40
		print '\033[2J'
		Casino_office='''
\033[{12};{11}H{0}{6}+-------------------------------------------------+
\033[{13};{11}H{0}{6}|{7}    {8}{1}|{1}{9}  Pickle Rick\'s Casino Loan Office  {8}{1}|{7}       {6}{0}|
\033[{14};{11}H{0}{6}|{7}    {8}{1}|{1}{9}    Current Rate :  {28}            {8}{1}|{7}       {6}{0}|
\033[{15};{11}H{0}{6}|{7}    {8}{1}|{1}{9}                                    {8}{1}|{7}       {6}{0}|
\033[{16};{11}H{0}{6}|{7}    {8}{1}+____________________________________+{7}       {6}{0}|
\033[{17};{11}H{0}{6}|{7}                                                 {6}{0}|
\033[{18};{11}H{0}{6}|{7}      {5}1: Pay Your Debt!                          {6}{0}|
\033[{19};{11}H{0}{6}|{7}      {5}2: Get A Loan!                             {6}{0}|
\033[{20};{11}H{0}{6}|{7}      {5}3: Go Back To Casino                       {6}{0}|
\033[{21};{11}H{0}{6}|{7}                                                 {6}{0}|
\033[{22};{11}H{0}{6}|{7}                                                 {6}{0}|
\033[{23};{11}H{1}{8}+-------------------{9}{10}________{1}{8}----------------------+
\033[{24};{11}H{1}{8}|{6}                  {9}{10}/ |  | | \{6}                     {1}{8}|
\033[{25};{11}H{1}{8}|{6}                 {9}{10}/| |  | | |\{6}                    {1}{8}|
\033[{26};{11}H{1}{8}+-------------------------------------------------+{3}{4}
\033[{27};{11}H Player Case Balance : {29}
\033[{31};{11}H Player Debt Balance : {30}'''.format(self.BLACK,self.WHITE,self.NO_COLOUR,self.BLACKBKGD,self.BLUE,self.GREEN,self.WHITEBKGD,self.GREYBKGD,self.BLUEBKGD,self.GREENBKGD,self.GREY,y,x,x+1,x+2,x+3,x+4,x+5,x+6,x+7,x+8,x+9,x+10,x+11,x+12,x+13,x+14,x+15,self.CurrentRate,self.PlayerCash,self.PlayerDebt,x+16)
		print Casino_office

	def Make_Payment(self):
		x = 22
		y = 30
		payment_made = False
		while payment_made != True:
			try:
				payment = input('\033[{0};{1}H{2}HHow Much would you like to pay? : '.format(x,y,self.BLUE))
			except:
				payment_made == False
				print '\033[{0};{1}H{2}Thats not a valid payment!'.format(x+1,y,self.RED)

			if int(payment) < int(self.PlayerCash):
				print '\033[{0};{1}H{2}Thank you for your payment!'.format(x+1,y,self.BLUE)
				payment_made == True
				self.PlayerDebt = self.PlayerDebt - payment
				self.PlayerCash = self.PlayerCash - payment
				return(self.PlayerCash,self.PlayerDebt)
			else:
				payment_made == False
				print '\033[{0};{1}H{2}What are you trying to pull? You don\'t have that ammount!'.format(x+1,y,self.RED)

	def Take_Loan(self):
		loan_accepted = None
		x = 22
		y = 30
		while loan_accepted != True:
			try:
				loan_ammount = input('\033[{0};{1}H{2}How much would you like to take? : '.format(x,y,self.BLUE))
			except:
				print '\033[{0};{1}H{2}Thats not a valid loan ammount!'.format(x+1,y,self.RED)
				validloan = False
				loan_ammount = 0
				continue

			if loan_ammount <= 1000000 and loan_ammount > 0:
				print '\033[{0};{1}H{2}The load officer accepts your application and approves you for a loan at {3}'.format(x+1,y,self.GREEN,self.CurrentRate)
				self.PlayerCash = loan_ammount + self.PlayerCash
				self.PlayerDebt = loan_ammount + (loan_ammount * self.CurrentRate) + self.PlayerDebt
				loan_accepted = True
			else:
				print '\033[{0};{1}H{2}Thats not an acceptable loan ammount'.format(x+1,y,self.RED)
				loan_ammount = 0
				loan_accepted = False
	def Menu(self):
		x = 22
		y = 30
		LeaveMenu= None
		while LeaveMenu != 3:
			self.Print_Office()
			try:
				selection = input('\033[{0};{1}H{2}HPlease Make Your Selection? : '.format(x,y,self.BLUE))
			except:
				print '\033[{0};{1}H{2}Thats not a valid Selection!'.format(x+1,y,self.RED)
			if selection == 1:
				if self.PlayerDebt > 0:
					self.Make_Payment()
				else:
					print '\033[{0};{1}H{2}You don\'t have a loan currently!'.format(x+1,y,self.RED)
			if selection == 2:
				self.Take_Loan()
			if selection == 3:
				return(self.PlayerCash,self.PlayerDebt)
		return(self.PlayerCash,self.PlayerDebt)
