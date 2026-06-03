print("Welcome to the bank!")
balance = 1000
while True:
        print("what would you like to do?")
        print("1. check balance")
        print("2. deposit")         
        print("3. withdraw")
        print("4. exit")
        type = input("enter the number corresponding to your choice: ")
        
        if type == "4":
            print("bye!") 
            break 
        elif type == "1":
            print(f"you have ${balance} in your account")
        elif type == "2":
            deposit = int(input("how much amount would you like to deposit?"))
            balance = int(balance) + deposit
            print(f"you have deposited ${deposit} and now have a new balance of ${balance:}")
        elif type == "3":
                withdraw = float(input("how much would you like to withdraw?"))
                if withdraw <= int(balance):
                    balance = int(balance) - withdraw
                    print(f"you withdrawed ${withdraw} and now your balance is ${balance:}")
                else:
                    print("you dont have enough funds in your bank account")

else:
        print("invalid option, plz try again")
