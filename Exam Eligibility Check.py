medical=input("Do you have a medical cause Y or N:").upper()
atten=input("Is your attendance more than 75% Y or N:").upper()

if medical=='Y':
    print("You can do the exam")
else:
    if atten=='Y':
        print("You can do the exam")
    else:
        print("You can't do the exam")