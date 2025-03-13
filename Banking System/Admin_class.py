from Bank_class import Bank
from Account_class import Account_holder


class Admin(Account_holder, Bank):
    
    def __init__(self, name, key):
        self.name = name
        self.key = key
        
    def Freeze_account():
        '''Just disable account from file'''
        pass
    
    def Close_account():
        '''Just erase Account from file'''
        pass
    
    def Creating_account():
        '''Will create account/signup and insert info 
            to file for verify'''
        '''This function will take name, email, address for 
            account creation'''
        print("++ Create Account ++")
        Account_holder.name = input("Name: ")
        Account_holder.address = input("Address: ")
        Account_holder.email = input("Email: ")
        Bank.Card_num = input("Card Number: ")
        print("^Only Last Four Digits^")
    
    def signup():
        '''Will only need email and name then user can create 
            password/username/Card_num for login'''
        pass
    
    def admin_menu():
        '''Need a menu for Admin nav'''
        print("+---Welcome Admin---+")
        print("| 1. Freeze Account |")
        print("| 2. Close Account  |")
        print("| 3. Create Account |")
        print("+-------------------+")