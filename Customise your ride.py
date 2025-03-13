print("Select your ride: ")
print("1. Bike\n2. Car\n")
choice=int(input("Enter your choice: "))

if choice==1:
    print("What type of bike?")
    print("1. Bicycle\n2. Motorbike\n")
    choice2=int(input("Enter your choice: "))
    if choice2==1:
        print("You have chosen a Bicycle")
    else:
        print("You have chosen a Motorbike")
elif choice==2:
    print("What type of Car?")
    print("1. Mercedes\n2. BMW\n")
    choice3=int(input("Enter your choice: "))
    if choice3==1:
        print("You have chosen a Mercedes")
    else:
        print("You have chosen a BMW")