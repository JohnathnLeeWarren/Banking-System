from Bank_class import Bank


class Account_holder(Bank):
    
    def __init__(self, name, address, email, account_num):
        self.name = name
        self.address = address
        self.email = email
        self.account_num = account_num