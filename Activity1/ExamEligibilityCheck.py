medicalcause= input("Do you have a medical cause??(Y/N)").strip().upper()


if medicalcause=="Y":
    print("You can proceed.")
else:
    attendence=int(input("What is your attendance percentage??"))
    if attendence>=75:
        print("You can proceed.")
    else:
        print("You cannot proceed.")