if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <=12:
        print("you have to pay $2")
    elif age <= 18:
        print("you have to pay $4")
    elif age <= 21:
        print("you have to pay $5")
    else:
        print("you have to pay $6")

else:
    print("Sorry you have to grow taller before you can ride.")