def show_balance(balance):
    print(f"your balance is: {balance:.2f}dzd")
def deposit(balance , deposit_amount):
    if deposit_amount < 0:
        print("u can't deposit a negative amount of money!")
    else:
        balance += deposit_amount
    return balance
def withdraw(balance , withdraw_amount):
    if withdraw_amount < 0:
        print("u can't withdraw a negative amount of money!")
    else:
        balance -= withdraw_amount
    return balance
balance = 0.00
option = ""
while option == "":
    print("====================================")
    print("              Bank                  ")
    print("====================================")
    print()
    print("what do u want to do?")
    print("1. see balance") 
    print("2. deposit")
    print("3. withdraw")
    print("4. quit")
    print()
    print("=====================================")
    print("=====================================")
    option = input("enter the number of the option: ")
    print()
    print("=====================================")
    print()
    if option not in ["1" ,"2" ,"3" ,"4"]:
        print("invalid choice!")
        option = ""
    else:
        option = int(option)
        if option == 1:
            show_balance(balance)
        elif option == 2:
            deposit_amount = float(input("enter the amount of money u want to deposit in dzd: "))
            balance = deposit(balance , deposit_amount)
        elif option == 3:
            withdraw_amount = float(input("enter the amount of money u want to withdraw in dzd: "))
            if withdraw_amount > balance:
                print("u don't have much money!")
            else:
             balance = withdraw(balance , withdraw_amount)

        else:
            print("take care !")
            break
    option = ""
