print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Would you like to see the photo? (Yes/No): ")
    if wants_photo == "Yes":
        bill += 10

    print("Your total bill is $" + str(bill))

else:
    print("Sorry you have to grow taller before you can ride.")
