from Account_class import Account_holder
from Admin_class import Admin
import main

class Bank:
    amount = float
    deposit = float
    withdraw = float
    result = float
    
    def __init__(self, name, contact, Card_num):
        self.name = name
        self.contact = contact
        self.Card_num = Card_num
        
    def account_amount():
        print("$ " + Bank.amount)
        
    def deposit():
        Bank.deposit = input("How much: $ ")
        
        Bank.deposit + Bank.amount = Bank.result
        
        return Bank.result
    
    def withdraw():
        Bank.withdraw = input("How much: $ ")
        
        Bank.amount - Bank.withdraw = Bank.result
        
        return Bank.result
    
    def transfer():
        Account_holder.account_num = input("Account Number: ")
        yes_no = input("Are you sure you want to transfer " + Bank.amount + " to Account Number " + Account_holder.account_num + "?\n 1.Yes or 2.No\n " + " -> ")
        
        if yes_no == 1 | "1":
            Bank.amount + Bank.amount = Bank.result
        else:
            print("Canceled")
    
    def verify_account():
        '''This will only verify Login in file'''
        pass
    
    def login():
        print("--Login--")
        username = input("Username: ")
        password = input("Password: ")
        
        if username == "Admin":
            if password == "00":
                Admin.admin_menu()
    
    def signup_verify():
        '''This will only verify Account holder in file'''
        '''This will send an email to verify account'''
        pass