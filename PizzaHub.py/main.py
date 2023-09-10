import time

print("Welcome to Greg's Pizza Hub\n")
sizePizza = input("Please select Size of Pizza: (S / M/ L ):\n").lower()
pepperoni = input("Would you like to add pepperoni (Y / N) ):  ").lower()
cheese = input("Would you like to add cheese to your order: (Y / N ): ").lower()

bill = 0

if sizePizza == 's':
    if pepperoni == 'y':
        if cheese == 'y':
            bill = 20
            print("Your order will consist of a Small pizza with pepperoni, with Cheese")
        else:
            bill = 15
            print("Your order will consist of a Small pizza with pepperoni, without Cheese")
    else:
        bill = 10
        print("Your order will a be Small pizza")

elif sizePizza == 'm':
    if pepperoni == 'm':
        if cheese == 'l':
            bill = 30
            print("Your order will consist of a Medium pizza with pepperoni, with Cheese")
        else:
            bill = 25
            print("Your order will consist of a Medium pizza with pepperoni, with Cheese")
    else:
        bill = 20
        print("Your order will be a Medium pizza")
elif sizePizza == 'l':
    if pepperoni == 'y':
        if cheese == 'y':
            bill = 40
            print("Your order will consist of a Large pizza with pepperoni, with Cheese")
        else:
            bill = 35
            print("Your order will consist of a Large pizza with pepperoni, with Cheese")
    else:
        bill = 30
        print("Your order will be a Large pizza")

time.sleep(3)
print(f'Total Bill: R {bill}\nThank you !!!!!!!!, for the support')




