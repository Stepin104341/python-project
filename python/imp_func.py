import pickle
import os
import pathlib
from classes import Account

def writeAccount():
    account = Account()
    account.createAccount()
    writeAccountsFile(account)



def writeAccountsFile(account) : 
    
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.data')
    else :
        oldlist = [account]
    outfile = open('changedAcc.data','wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('changedAcc.data', 'accounts.data')       

def displaySp(num): 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist :
            if item.Account_number == num :
                print("Balance in your account is  = ",item.deposit)
                found = True
    else :
        print("No records present in the file")
    if not found :
        print("No records with this account number found ")

def depositAndWithdraw(num1,num2): 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist :
            if item.Account_number == num1 :
                if num2 == 1 :
                    amount = int(input("Amount to be deposited into the account is  : "))
                    item.deposit += amount
                    print("Amount status updated ")
                elif num2 == 2 :
                    amount = int(input(" THE AMOUNT TO BE WITHDRAWN IS   : "))
                    if amount <= item.deposit :
                        item.deposit -=amount
                    else :
                        print("Amount in the account is less than the withdrawn amount please chnage the value to be withdrawn")
                
    else :
        print("No records found ")
    outfile = open('changedAcc.data','wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('changedAcc.data', 'accounts.data')

    
def deleteAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for item in oldlist :
            if item.Account_number != num :
                newlist.append(item)
        os.remove('accounts.data')
        outfile = open('changedAcc.data','wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('changedAcc.data', 'accounts.data')
     
def modifyAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in oldlist :
            if item.Account_number == num :
                item.name = input("Enter the account holder name : ")
                item.type = input("Enter the account Type : ")
                item.deposit = int(input("Enter the Amount : "))
        
        outfile = open('changedAcc.data','wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('changedAcc.data', 'accounts.data')
   
def displayAll():
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        for item in mylist :
            print(item.Account_number," ", item.name, " ",item.type, " ",item.deposit )
        infile.close()
    else :
        print("No Records are found")
