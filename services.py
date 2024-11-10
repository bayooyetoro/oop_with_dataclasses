import sqlite3
from logics import *
import sys

def process_input(account):
   while True:
        load_services()
        service = input("\nEnter a Service Number: ")

        if service.lower() == 'a':
            account.get_balance()

        elif service.lower() == 'b':
            amount = int(input("Enter Amount: "))
            account.deposit(amount)

        elif service.lower() == 'c':
            amount = int(input("Enter Transfer Amount: "))
            account.transfer(amount)

        elif service.lower() == 'd':
            amount = int(input("Enter Withdraw Amount: "))
            account.withdraw(amount)
  
        elif service.lower() == 'e':
            sys.exit("Goodbye!")