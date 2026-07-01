Pass = 1234
user_balance=5000
pin = int(input("Enter Your PIN: "))

if pin == Pass:
    process=int(input("Choose Process:\n(1)Withdraw\n(2)Check Balance\nNumber Of Process: "))
    
    if process == 1 :
        withdrawl_amount=int(input("Enter Withdrawl Amount: "))
        if withdrawl_amount <= user_balance:
            user_balance-=withdrawl_amount
            print(f"Done. Your balance is : {user_balance}")
        else:
            print("Sorry, Your balanece not enough")
             
    elif process == 2:
            print(f"Your Balance :{user_balance}")

else:
    print("Sorry ,Wrong PIN !")    