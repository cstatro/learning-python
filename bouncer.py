age = input("how old are you:")
if age:
    if int(age) >= 18 and int(age) < 21:
        print("You need a wristband")
    elif int(age) >= 21:
        print("You can come in and drink")
    else:
        print("you can't come in")
else:
    print("enter a valid age")
