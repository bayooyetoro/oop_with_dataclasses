from dataclasses import *
import random 
import string

def open_msg():
    print("-"*50)
    print("Welcome to TerminalBank. Let's create your account")
    print("-"*50)
    
@dataclass
class Account:
    def generateAccountNo():
       return "".join(random.choice(string.digits) for _ in range(10))
    
    name: str
    email: str
    balance: int = field(default=0, repr=False)#= field(default=0, repr=False)
    accountNo : str = field(default=generateAccountNo(), init=False)


    def transfer(self, amount):
        if self.balance >= amount:
          self.balance -= amount 
          print(f"${amount} Transferred!\nNew Balance: ${self.balance}")
        else:
            print("Failed!. Insufficient funds Balance")


    def withdraw(self, amount):
        if self.balance >= amount:
          self.balance -= amount 
          print(f"${amount} Withdrew!\nNew Balance: ${self.balance}")
        else:
            print("Failed!. Insufficient funds Balance")


    def get_balance(self):
        print(f"\nAvailable Balance: ${self.balance}\n")
    

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount} successfully!")
        print(f"Balance: ${self.balance}\n")


def open_account():
    name = input("What is your name?: ")
    email = input("Type your email address: ")
    return Account(name, email)


def load_services():
    print("Press A to >> Check Balance")
    print("Press B to >> Deposit")
    print("Press C to >> Transfer")
    print("Press D to >> Withdraw")
    print("Press E to >> Exit wallet")
    

  
        
    


