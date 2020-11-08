from classes import *
from imp_func import *
 
# start of the program
ch=''
num=0
print("\t\t\t\t**********************")
print("\t\t\t\tOnline Bnking System")
print("\t\t\t\t**********************")
'''input("Press any key to continue")'''
while ch != 8:
    print("\t1. Press 1 to create an account ")
    print("\t2. Press 2 to deposit amount into an account")
    print("\t3. Press 3 to withdraw an mount from the account number ")
    print("\t4. Press 4 for balance enquiry")
    print("\t5. Press 5 for all account details")
    print("\t6. Press 6 to close an account ")
    print("\t7. Press 7 to modify an account")
    print("\t8. Press 8 to exit the code")
    print("\tPick an element from  (1-8) ")
    ch = input() 
    if ch == '1':
        writeAccount()
    elif ch =='2':
        num = int(input("\tEnter The account No. : "))
        depositAndWithdraw(num, 1)
    elif ch == '3':
        num = int(input("\tEnter The account No. : "))
        depositAndWithdraw(num, 2)
    elif ch == '4':
        num = int(input("\tEnter The account No. : "))
        displaySp(num)
    elif ch == '5':
        displayAll();
    elif ch == '6':
        num =int(input("\tEnter The account No. : "))
        deleteAccount(num)
    elif ch == '7':
        num = int(input("\tEnter The account No. : "))
        modifyAccount(num)
    elif ch == '8':
        print("\tThanks for using bank managemnt system")
        break
    else :
        print("Invalid choice")
    
    ch = input("Enter your choice : ")
    


    
    
    
    
    
    
    
    
    
    
