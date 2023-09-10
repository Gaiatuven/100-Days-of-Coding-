leap_year = int(input("Which year do you want to check: "))

if leap_year % 4 == 0:
    if leap_year % 100 == 0:
        if leap_year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year.")
    else:
        print("Leap year")
else:
    print("Not a leap year.")
