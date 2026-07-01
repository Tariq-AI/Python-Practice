print("------WELCOME------")

price = int(input("Enter The Price : "))

if price < 100:
    print(f"The Discount : 0% ,Total Price = {price}")
elif price < 500:
    print(f"The Discount : 10% ,Total Price = {price - price*10/100}")
elif price >= 500:
    print(f"The Discount : 20% ,Total Price = {price - price*20/100}")
