print("Select your ride:")
print("1.Bike")
print("2.Car")
Choice=int(input("Enter you choice:(1/2)"))
if(Choice==1):
    print("Choose your Bike:")
    print("1.Scooty")
    print("2.Motorcycle")
    Choice2=int(input("Enter you choice:(1/2)"))
    if Choice2==1:
        print("You have chosen a Scooty as your ride.")
    else:
        print("You have chosen a Motorcycle as your ride.")



if(Choice==2):
    print("Choose your Car:")
    print("1.Sedan")
    print("2.SUV")
    Choice2=int(input("Enter you choice:(1/2)"))
    if Choice2==1:
        print("You have chosen a Sedan as your ride.")
    else:
        print("You have chosen a SUV as your ride.")