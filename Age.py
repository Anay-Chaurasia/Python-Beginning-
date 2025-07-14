age=int(input("Enter You'r Age"))
if age < 18:
    print("Not Eligible for voting")
else:
    print("Eligible for Voting")
    a=str(input("Do you have a license?"))
    if a.strip().lower()== "y":
        print("You can drive a car")
    else:
         print("You can't drive a car")