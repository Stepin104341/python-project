
import pickle
import os
import pathlib
class Account :
    Account_number = 0
    name = ''
    deposit=0
    type = ''
    
    def createAccount(self):
        self.Account_number= int(input("Please enter the account number : "))
        self.name = input("Please enter the name of the account holder : ")
        self.type = input("Ente the type of account Current(c) savings(s)[C/S] : ")
        self.deposit = int(input("Enter The Initial amount"))
        print("\n\nAccount Created sucessfully ")
    
    def showAccount(self):
        print("Account Number : ",self.Account_number)
        print("Account Holder Name : ", self.name)
        print("Type of Account",self.type)
        print("Balance : ",self.deposit)
    
    def modifyAccount(self):
        print("Account Number : ",self.Account_number)
        self.name = input("Modify Account Holder Name :")
        self.type = input("Modify type of Account :")
        self.deposit = int(input("Modify Balance :"))
        
    def depositAmount(self,amount):
        self.deposit += amount
    
    def withdrawAmount(self,amount):
        self.deposit -= amount
    
    def report(self):
        print(self.Account_number, " ",self.name ," ",self.type," ", self.deposit)
    
    def getAccountNo(self):
        return self.Account_number
    def getAcccountHolderName(self):
        return self.name
    def getAccountType(self):
        return self.type
    def getDeposit(self):
        return self.deposit




