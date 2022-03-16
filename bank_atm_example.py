class Account:
    def __init__(self,owner,balance = 0):
        self.owner = owner
        self.balance = balance
    def __str__(self):
        return f"Account owner: {self.owner} \nAccount balance: {self.balance}"
    def deposit(self,deposit):
        self.balance += deposit
        print("Deposit Accepted")
    def withdraw(self,withdraw):
        if self.balance >= withdraw:
            self.balance -= withdraw
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')

print("Welcome the Boss Bank ")
name = input("Enter the name: ")
balance = int(input("Enter the deposit value: "))
account = Account(name,balance)
bank_screen= True
while bank_screen:
    choise = int(input("What operation do you want to take? \n Press 1 Deposit operation \n Press 2 Withdraw operation \n Press 3 Check bank account \n Press 4 Exit \n Enter the number: "))
    if choise == 1:
        dp_value = int(input("Enter the deposit value: "))
        account.deposit(dp_value)
    elif choise == 2:
        wd_value = int(input("Enter the withdraw value: "))
        account.withdraw(wd_value)
    elif choise == 3:
        print(str(account))
    elif choise == 4:
        break

            