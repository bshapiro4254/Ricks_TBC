from colorama import init
import random
import sys
import os
import csv
import datetime
from Ricks_Casino_Loan_Office import Ricks_Casino_Loan_Office as Ricks_CLO

class Player_Saves():
    def __init__(self,P_Cash,P_Debt,P_Bank,P_Account_Data):
        init()
        now = datetime.datetime.now()
        if P_Account_Data != None:
            self.P_AccountData = P_Account_Data
            self.P_Account = int(P_Account_Data['Account'])
            self.PW = P_Account_Data['PW']
            self.P_FName = P_Account_Data['P_FName']
            self.P_LName = P_Account_Data['P_LName']
        else:
            self.P_AccountData = None
            self.P_Account = None
            self.P_FName = None
            self.P_LName = None
            self.PW = None

        self.PlayerCash = P_Cash
        self.PlayerDebt = P_Debt
        self.PlayerBank = P_Bank
        self.CurrentDate = {'Year':now.year,'Month':now.month,'Day':now.day,'Hour':now.hour}
        self.IsLoaded = False
        self.P_Save_Dict={}
        if os.path.exists("Ricks_Accounts.csv"):
            print 'Save Data Found, Loading File...'
            self.SaveFile = open("Ricks_Accounts.csv", "r")
            reader = csv.reader(self.SaveFile)
            count = 0
            for rows in reader:
                if count == 0:
                    self.P_Save_Dict={}
                Temp_Line = {'Account':int(rows[0]),'P_FName': rows[1],'P_LName': rows[2],'P_Cash': float(rows[3]),'P_Debt': float(rows[4]),'P_Bank': float(rows[5]),'PW':rows[6],'Last_Played':{'Year':int(rows[7]),'Month':int(rows[8]),'Day':int(rows[9]),'Hour':int(rows[10])}}
                #print Temp_Line
                count += 1
                self.P_Save_Dict[int(rows[0])]={}
                self.P_Save_Dict[int(rows[0])].update(Temp_Line)
                print self.P_Save_Dict
                self.SaveEmpty = False
            self.SaveFile.close()
        else:
            print 'No Save Data Found, Creating File...'
            self.SaveFile = open("Ricks_Accounts.csv", "w")
            self.P_Save_Dict = {}
            self.SaveEmpty = True
            self.SaveFile.close()

    def ReInit_Account(self):
        if self.P_AccountData != None:
            #print self.P_AccountData
            for key,value in self.P_AccountData.items():
                self.P_Account = key
            #print self.P_Account
            self.PW = self.P_AccountData['PW']
            self.P_Account = self.P_AccountData['Account']
            self.P_FName = self.P_AccountData['P_FName']
            self.P_LName = self.P_AccountData['P_LName']
            self.PlayerCash = self.P_AccountData['P_Cash']
            self.PlayerDebt = self.P_AccountData['P_Debt']
            self.PlayerBank = self.P_AccountData['P_Bank']

    def Create_Account(self):
        print 'Welcome To Pickle Rick\'s VIP Member Program!'
        acctandpw = False
        acct = None
        PW = None
        P_FName = None
        P_LName = None
        if self.P_Account > 0:
            print 'You Already have an account.'
            return
        while acctandpw == False:
            try:
                if self.P_FName == None:
                    self.P_FName = raw_input('Enter your First Name. : ')
                    yn = raw_input('{0}, Is this Correct?Y/n: '.format(self.P_FName))
                    if yn.upper() == 'Y':
                        print
                    elif yn.upper() == 'N':
                        print 'Let\'s Try Again.'
                        self.P_FName = None
                        yn = None
                        continue

                if self.P_LName == None:
                    self.P_LName = raw_input('Enter your Last Name. : ')
                    yn = raw_input('{0}, Is this Correct?Y/n: '.format(self.P_LName))
                    if yn.upper() == 'Y':
                        print
                    elif yn.upper() == 'N':
                        print 'Let\'s Try Again.'
                        self.P_LName = None
                        yn = None
                        continue

                if acct == None:
                    acct = input('Select An Acct #: ')
                    isused = False
                    if len(self.P_Save_Dict) > 0:
                        for key, value in self.P_Save_Dict.items():
                            if int(key) == int(acct):
                                'The Account Number {0} is taken, Sorry!'.format(str(acct))
                                isused = True
                                acct = None
                                continue
                    else:
                        isused = False

                    if isused == False:
                        'Your Acct # Will Be : {0}'.format(str(acct))
                        self.P_Account = int(acct)
                    else:
                        'The Account Number {0} is taken, Sorry!'.format(str(acct))
                        acct = None
                        continue

                if self.PW == None:
                    pw1 = raw_input('Enter your New Password: ')
                    pw2 = raw_input('ReEnter your New Password: ')
                    if pw1.upper() == pw2.upper():
                        print 'Your Password is Set!'
                        self.PW = pw1

                    else:
                        print 'Passwords do not match. Try Again!'
                        self.PW = None
                        pw1 = None
                        pw2 = None
                        continue
                if self.PW != None and self.P_Account != None:
                    acctandpw = True
            except:
                print 'There was a Problem with your Entry! Try again!'
                continue
        self.P_AccountData = {}
        self.P_AccountData = {}
        self.P_AccountData.update({'Account': acct,'P_FName': self.P_FName,'P_LName': self.P_LName,'P_Cash': self.PlayerCash,'P_Debt': self.PlayerDebt,'P_Bank': self.PlayerBank,'PW':self.PW,'Last_Played': self.CurrentDate})
        self.P_Save_Dict[acct] = {}
        self.P_Save_Dict[acct].update({'Account': acct,'P_FName': self.P_FName,'P_LName': self.P_LName,'P_Cash': self.PlayerCash,'P_Debt': self.PlayerDebt,'P_Bank': self.PlayerBank,'PW':self.PW,'Last_Played': self.CurrentDate})
        self.Write_Save()
        self.ReInit_Account()

    def Load_Game(self):
        acct = None
        while acct == None:
            try:
                acct = input('Enter Your Account Number! : ')
            except:
                print 'That is not a valid Player Account number!'
                acct = None
                continue
            isused = True
            if len(self.P_Save_Dict) > 0:
                for key, value in self.P_Save_Dict.items():
                    try:
                        if int(key) == int(acct) :
                            'We Found Your Account. Number {0}!'.format(str(acct))
                            isused = False
                    except:
                        print 'That is not a valid Player Account number!'
                        isused = True
                        acct = None
                        continue

            else:
                isused = True
                acct = None
                continue
            if isused == True:
                print 'Account Number Not Found!'
                selection = ''
                while selection.upper() not in ['Q','C','A']:
                    selection = raw_input('''Try entering again   - A
Create A New Account - C
Give Up              - Q
Make Your Selection: ''')
                    if selection.upper() == 'Q':
                        print 'Heading Back to The Casino'
                        return

                    elif selection.upper() == 'A':
                        print 'Trying to Load Again!'
                        self.Load_Game()
                        return
                    elif  selection.upper() == 'C':
                        print 'Let\'s Create An Account For You!'
                        self.Create_Account()
                        return
            if isused == False:
                Player_Acct_Info = self.P_Save_Dict[acct]
                correct_pw = False
                while correct_pw == False:
                    try:
                        EPW = raw_input('Enter your Account Password!')
                    except:
                        correct_pw = False
                    if EPW.upper() == Player_Acct_Info['PW'].upper():
                        P_FName = Player_Acct_Info['P_FName']
                        print 'Welcome {0}. Your Password is Correct. Loading Account!'.format(P_FName)
                        self.P_AccountData = {}
                        self.P_AccountData = {}
                        self.P_AccountData.update(Player_Acct_Info)
                        self.P_Save_Dict[acct].update(Player_Acct_Info)
                        self.Write_Save()
                        return
                    else:
                        print 'You Entered an incorrect PassWord!'
                        EPW = None
                        correct_pw = False
                        continue


    def Save_Game(self):
        use_stored = True
        acct = None
        if self.P_Account == None:
            print 'You Don\'t Have an Account, Please Load or Create one to Save'
            return

        while acct == None:
            if self.P_Account != None and use_stored == True:
                acct = int(self.P_Account)
                use_stored = False
            else:
                acct = None

                try:
                    acct = input('Enter Your Account Number')
                except:
                    print 'That is not a valid Player Account number!'
                    acct = None
                    continue
            if len(self.P_Save_Dict) > 0:
                for key, value in self.P_Save_Dict.items():
                    if int(key) == int(acct):
                        'We Found Your Account. Number {0}!'.format(str(acct))
                        isused = False

            else:
                isused = True
                acct = None
                continue

            if isused == True:
                print 'Account Number Not Found!'
                selection = None
                while selection.upper not in ['Q','C','A']:
                    selection = raw_input('''Try entering again   - A
Create A New Account - C
Give Up              - Q
Make Your Selection: ''')
                    if selection.upper() == 'Q':
                        print 'Heading Back to The Casino'
                        return

                    elif selection.upper() == 'A':
                        print 'Trying to Save Again!'
                        self.Save_Game()
                        return
                    elif  selection.upper() == 'C':
                        print 'Let\'s Create An Account For You!'
                        self.Create_Account()
                        return

            if isused == False:
                Player_Acct_Info = self.P_Save_Dict[acct]
                correct_pw = False
                while correct_pw == False:
                    try:
                        EPW = raw_input('Enter your Account Password!')
                    except:
                        correct_pw = False
                    if EPW.upper() == Player_Acct_Info['PW'].upper():
                        P_FName = Player_Acct_Info['P_FName']
                        print 'Welcome {0}. Your Password is Correct. Saving Account!'.format(P_FName)
                        self.P_AccountData = {}
                        self.P_AccountData = {}
                        self.P_AccountData.update({'Account': acct, 'P_FName': self.P_FName,'P_LName': self.P_LName,'P_Cash': self.PlayerCash,'P_Debt': self.PlayerDebt,'P_Bank': self.PlayerBank,'PW':self.PW,'Last_Played': self.CurrentDate})
                        self.P_Save_Dict[acct] = {}
                        self.P_Save_Dict[acct].update({'Account': acct, 'P_FName': self.P_FName,'P_LName': self.P_LName,'P_Cash': self.PlayerCash,'P_Debt': self.PlayerDebt,'P_Bank': self.PlayerBank,'PW':self.PW,'Last_Played': self.CurrentDate})
                        self.Write_Save()
                        correct_pw = True
                        return
                    else:
                        print 'Your PassWord Entry was Incorrect! Try Again!'
                        EPW = None
                        correct_pw = False
                        continue


    def Write_Save(self):

        #if os.path.exists("Ricks_Accounts.csv"):
        firstline = 0
        self.ReInit_Account()
        for account, data in self.P_Save_Dict.items():
            if firstline == 0:
                self.SaveFile = open("Ricks_Accounts.csv", "w")
                firstline += 1
            elif firstline == 1:
                self.SaveFile = open("Ricks_Accounts.csv", "a")
                firstline += 1
            Temp_Line = '{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}\n'.format(account,data['P_FName'],data['P_LName'],data['P_Cash'],data['P_Debt'],data['P_Bank'],data['PW'],data['Last_Played']['Year'],data['Last_Played']['Month'],data['Last_Played']['Day'],data['Last_Played']['Hour'])
            self.SaveFile.write(Temp_Line)
            if firstline == 0:
                self.SaveFile.close()
        self.SaveFile.close()

    def Main_Save_Menu(self):
        MSM_Selection = None
        while MSM_Selection == None:
            print '''   Welcome to Pickle Rick\'s Casino:
        The Save Menu!
        Account # and PW required
            1. Save Your Game.
            2. Load Your Saved Game.
            3. Create a New account.
            4. Return to the Casino.'''
            try:
                MSM_Selection = input('Enter Your Selection. : ')
                if MSM_Selection > 4 or MSM_Selection < 1:
                    print 'That was not a valid Selection.'
                    MSM_Selection = None
                    continue
            except:
                print 'That was not a valid Selection.'
                MSM_Selection = None
                continue
            if MSM_Selection == 1:
                self.Save_Game()
                MSM_Selection = None
            elif MSM_Selection == 2:
                self.Load_Game()
                MSM_Selection = None
            elif MSM_Selection == 3:
                self.Create_Account()
                MSM_Selection = None
            elif MSM_Selection == 4:
                print 'You Return to the Casino Floor'
                self.Write_Save()
                return (self.PlayerCash,self.PlayerDebt,self.PlayerBank,self.P_AccountData)
