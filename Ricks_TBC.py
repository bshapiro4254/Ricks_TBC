from colorama import init
import re
import random
from Ricks_Casino_Loan_Office import Ricks_Casino_Loan_Office as Ricks_CLO
from Ricks_TCP import Three_Card_Poker
from Ricks_BJ import Black_Jack
from Save_Me_Rick import Player_Saves

def Play_Cards():
	print 'Evaluate the following cards and derive the sum.'
	My_Hand = Deal_Hand()
	H_Sum = Eval_Hand(My_Hand)
	print My_Hand
	Answer = raw_input('Enter your answer')
	if int(Answer) == int(H_Sum):
		print 'You are correct!!! The sum is {0}'.format(H_Sum)
	else:
		print 'You are incorrect!!! The sum is {0}'.format(H_Sum)

def old_Main():
	LetsPlay = raw_input('Do you want to Play a Game? Y/N/Q  :')
	if LetsPlay == 'Y' or LetsPlay == 'y':
		while LetsPlay.upper() != 'Q':
			Play_Cards()
			LetsPlay = raw_input('Enter Q to quit, Y to play again')

def Main():
	init()
	BLUE="\033[1;36m"
	RED="\033[1;31m"
	LIGHT_RED="\033[1;31m"
	WHITE="\033[1;37m"
	GREEN="\033[1;32m"
	NO_COLOUR="\033[0m"
	selection = None
	PlayerCash = 10000
	PlayerDebt = 0
	PlayerBank = 0
	Player_Acct_Info = None
	Spacing_BS = '                                           '

	S_Cash = Spacing_BS
	cut_space = 0
	cut_a_space = re.compile(r'^.')
	while cut_space < (len(list(str(PlayerCash)))):
		S_Cash = re.sub(cut_a_space,'',S_Cash)
		cut_space += 1

	S_Bank = Spacing_BS
	cut_space = 0
	while cut_space < (len(list(str(PlayerBank)))):
		S_Bank = re.sub(cut_a_space,'',S_Bank)
		cut_space += 1

	S_Debt = Spacing_BS
	cut_space = 0
	while cut_space < (len(list(str(PlayerDebt)))):
		S_Debt = re.sub(cut_a_space,'',S_Debt)
		cut_space += 1
	cut_space = 0

	while selection != 333:
		print '''	{4}------------------------------------------------------------
	{4}|		{1}Welcome to {0}Pickle Ricks {2}Casino!!!!{3}	   {4}|
	{4}|  {4}Please Choose your Game from the following List :{3}	   {4}|
	{4}|		{4}1. {0}BlackJack{3}				   {4}|
	{4}|		{4}2. {0}Three Card Poker{3}			   {4}|
	{4}|		{4}3. {0}Vist Ricks Casino Loan Office{3} 	   {4}|
	{4}|		{4}4. {0}Vist Ricks Casino Save n Load{3} 	   {4}|
	{4}|		{4}333. {0}Exit Ricks Casino{3}			   {4}|
	{4}------------------------------------------------------------
	{4}|	{0} Player Stats :					   {4}|
	{4}|	{1} Cash : {5}{8}{4}|
	{4}|	{2} Debt : {6}{9}{4}|
	{4}|	{3} Bank : {7}{10}{4}|
	{4}------------------------------------------------------------

			'''.format(GREEN,BLUE,LIGHT_RED,NO_COLOUR,WHITE,PlayerCash,PlayerDebt,PlayerBank,S_Cash,S_Debt,S_Bank)
		try:
			selection = input('Enter your Selection : ')
		except:
			print '{0}That is not a valid Selection!!!{1}'.format(RED,NO_COLOUR)
			selection == None
			continue
		if selection == 1:
			BlackJack_Game = Black_Jack(PlayerCash, PlayerDebt)
			(PlayerCash, PlayerDebt) = BlackJack_Game.Play_BJ()
		if selection == 2:
			TCP_Game = Three_Card_Poker(PlayerCash, PlayerDebt)
			(PlayerCash, PlayerDebt) = TCP_Game.Play_TCP()
		if selection == 3:
			RCLO = Ricks_CLO(PlayerCash, PlayerDebt)
			(PlayerCash, PlayerDebt) = RCLO.Menu()
		if selection == 4:
			SAVE = Player_Saves(PlayerCash, PlayerDebt, PlayerBank, Player_Acct_Info)
			(PlayerCash, PlayerDebt, PlayerBank, Player_Acct_Info) = SAVE.Main_Save_Menu()

Main()
