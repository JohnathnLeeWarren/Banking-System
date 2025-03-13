from Bank_class import Bank
from Account_class import Account_holder
from Admin_class import Admin
import os

main = True

while main:
    '''Menu Screen'''
    os.system('cls')
    print("+-- \033[4m-Banking System-\033[0m --+")
    print("| 1. Account Amount    |")
    print("| 2. Withdraw          |")
    print("| 3. Deposit           |")
    print("| 4. Transfer          |")
    print("| 5. Exit              |")
    print("+----------------------+")
    
    answer = int(input("-> "))
    
    if answer == 1:
        Bank.account_amount()
    elif answer == 2:
        Bank.withdraw()
    elif answer == 3:
        Bank.deposit()
    elif answer == 4:
        Bank.transfer()
    else:
        quit()