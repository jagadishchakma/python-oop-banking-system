from random import randint
class SonaliBank:
    bank_name = "Sonali Bank Ltd."
    bank_balance = 500000
    bank_loan_amount = 0
    bank_loan_possible = True
    bankrupt = False
    bank_user = {}
    bank_admin = {}


class User(SonaliBank):
    def __init__(self, name, email, address, account_type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_id = str(randint(100, 999))
        self.loan_times = 0
        super().bank_user[self.account_id] = {"name": self.name, "email": self.email, "address": self.address, "account_type": self.account_type, "balance": self.balance, "history": [], "loan_times": 0}
        print("..........................")
        print("Account Created Successfully!!")
        print(f"Welcome, {self.name} in {self.bank_name}")
        print("Now you can do:")
        print("..........................")
    
    def deposit(self, amount):
        self.balance += amount
        super().bank_user[self.account_id]["balance"] = self.balance
        super().bank_user[self.account_id]["history"].append(f"Deposit: {amount}")
        print("..........................")
        print(f"Deposite successfully!Amount of {amount} Tk.")
        print("..........................")
    
    def withdraw(self, amount):
        print("..........................")
        if self.balance < amount:
            print("Withdrawal amount exceeded")
        elif super().bankrupt == True:
            print(f"Oops! sorry now bank is bankrupt.So,{self.name} now can't possible withdraw.")
        else:
            self.balance -= amount
            super().bank_user[self.account_id]["balance"] = self.balance
            super().bank_user[self.account_id]["history"].append(f"Withdraw: {amount}")
           
            print(f"Withdraw Successfully! amount of {amount} Tk.")
        print("..........................")


    def check_balance(self):
        print("..........................")
        print(f"Available balance is: {super().bank_user[self.account_id]["balance"]} Tk.")
        print("..........................")
    def history(self):
        print("..........................")
        print(f"{self.name} Your Transaction History: ")
        for hist in  super().bank_user[self.account_id]["history"]:
            print(hist)
        print("..........................")
    
    def get_loan(self, amount):
        print("..........................")
        if super().bank_balance < amount:
            print("Oops! sorry the bank balance insufficient now.")
        elif super().bankrupt == True:
            print(f"Oops! sorry now bank is bankrupt.So,{self.name} now can't possible get loan.")
        elif super().bank_loan_possible == False:
            print(f"Sorry, now bank loan features unavailable!!")
        elif self.loan_times > 1:
            print(f"Oops! sorry {self.name} your loan limit excceded up to 2 times.")
        else:
            SonaliBank.bank_balance -= amount
            SonaliBank.bank_loan_amount += amount
            self.balance += amount
            self.loan_times += 1
            SonaliBank.bank_user[self.account_id]["balance"] = self.balance
            SonaliBank.bank_user[self.account_id]["loan_times"] = self.loan_times
            SonaliBank.bank_user[self.account_id]["history"].append(f"Get loan: {amount}")
            print(f"You've recieve get loan amount of {amount} Tk.")
        print("..........................")
    def balance_transfer(self, amount, account_to):
        print("..........................")
        if self.balance < amount:
            print("Oops! sorry your balance insufficient now.")
        elif super().bankrupt == True:
            print(f"Oops! sorry now bank is bankrupt.So,{self.name} now can't possible balance transfer.")
        elif account_to not in super().bank_user:
            print(f"Account does not exist")
        else:
            self.balance -= amount
            super().bank_user[self.account_id]["balance"] = self.balance
            super().bank_user[self.account_id]["history"].append(f"Balance transfer to {super().bank_user[account_to]["name"]}: {amount}")
            super().bank_user[account_to]["history"].append(f"Balace recieve from {self.name}: {amount}")
            super().bank_user[account_to]["balance"] += amount
          
            print(f"Balance transfer successfully to account {super().bank_user[account_to]["name"]}!")
        print("..........................") 


    def userActionInstruction(self):
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance Check")
        print("4. History")
        print("5. Get loan")
        print("6. Balance Transfer")
        print("7. Back")

class Admin(SonaliBank):
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        self.account_id = randint(100,999)
        super().bank_admin[self.account_id] = {"name": self.name, "email": email, "account_id": self.account_id}
        print(".............................")
        print("Admin account created successfully!")
        print(".............................")
    def adminActionInstruction(self):
        print("1. Delete user account")
        print("2. See all user account")
        print("3. Check total avialable bank balance")
        print("4. Check the total loam amount")
        print("5. On or off loan feature")
        print("6. Back")
    def delete_user_account(self, account_id):
        print(".......................")
        if account_id in super().bank_user:
            del super().bank_user[account_id]
            print(f"Provided account deleted successfully. Account id is: {account_id}")
        else:
            print("Account id was not found!")
        print(".......................")
    def see_all_user(self):
        print(".......................")
        for key,value in SonaliBank().bank_user.items():
            print(f"Accound_id: {key}, Account_Info: {value}")
        print(".......................")
    def bank_balance_check(self):
        print("..............................")
        print(f"Available bank balance is: {self.bank_balance}")
        print("..............................")
    def bank_loan_check(self):
        print("..............................")
        print(f"Total loan amount of {self.bank_loan_amount}")
        print("..............................")
    def bank_loan_feature(self, onOfOption):
        print("..................")
        SonaliBank.bank_loan_possible = True if onOfOption == 1 else False
        print(f"Bank loan feature successfully {"ON" if SonaliBank.bank_loan_possible == 1 else "OFF"}")
        print("..................")

while True:
    print(f"Welcome to {SonaliBank.bank_name}")
    print("1. Admin")
    print("2. User")
    print("3. Exit")
    option = int(input("Enter Options: "))
    if option == 1:
        print("1. Create an admin account")
        print("2. Back")
        adminOption = int(input("Enter option:"))
        if adminOption == 1:
            name = input("Input your name: ")
            email = input("Input your email: ")
            admin = Admin(name, email)
            while True:
                admin.adminActionInstruction()
                admin_account_option = int(input("Enter Option: "))
                if admin_account_option == 1:
                    delete_user_account_id = input("Enter delete user account id: ")
                    admin.delete_user_account(delete_user_account_id)
                elif admin_account_option == 2:
                    admin.see_all_user()
                elif admin_account_option == 3:
                    admin.bank_balance_check()
                elif admin_account_option == 4:
                    admin.bank_loan_check()
                elif admin_account_option == 5:
                    print("1. ON")
                    print("2. OFF")
                    onOfOption = int(input("Enter option: "))
                    admin.bank_loan_feature(onOfOption)
                elif admin_account_option == 6:
                    break
        else:
            pass
    elif option == 2:
        print("1. Create a account")
        print("2. Back")
        userOption = int(input("Enter option:"))
        if userOption == 1:
            name = input("Input your name: ")
            email = input("Inut your email: ")
            address = input("Input your address: ")
            print("1. Savings")
            print("2. Current")
            account_type = int(input("Select account types: "))
            user = User(name, email, address, account_type)
            while True:

                user.userActionInstruction()
                user_account_option = int(input("Enter Option: "))
                if user_account_option == 1:
                    deposite_amount = int(input("Enter deposit amount: "))
                    user.deposit(deposite_amount)
                elif user_account_option == 2:
                    withdraw_amount = int(input("Enter withdraw amount: "))
                    user.withdraw(withdraw_amount)
                elif user_account_option == 3:
                    user.check_balance()
                elif user_account_option == 4:
                    user.history()
                elif user_account_option == 5:
                    loan_amount = int(input("Enter laon amount: "))
                    user.get_loan(loan_amount)
                elif user_account_option == 6:
                    transfer_amount = int(input("Enter transfer amount: "))
                    account_to = input("Enter reciever bank id: ")
                    user.balance_transfer(transfer_amount, account_to)
                elif user_account_option == 7:
                    break
            
        elif userOption == 2:
            pass
    else:
        break
