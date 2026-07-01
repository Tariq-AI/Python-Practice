python= input("Experience with Python (yes , no): ").lower()
experience = int(input("Experience Years : "))
certificate =input("Graduated From CS or Completed Bootcamp (yes , no): ").lower()

if python == "yes" and (experience >= 2 or certificate == "yes"):
    print("Congartulations! you have been passed to the next stage.")
    
else:
    print("Sorry! Not Qualified.")
