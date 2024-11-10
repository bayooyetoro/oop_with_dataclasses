from logics import *
from services import *

def main():
    # displays the Home page
    open_msg()


    # Opens an Account for Users
    account = open_account()
    print(f"\nAccount Opened Successfully! Your Details here:")
    print(f"Account Name: {account.name}\nAccountNo: {account.accountNo}\n")


    # Process User Input
    process_input(account)
   

if __name__ == '__main__':
    main()