print("Welcome to the tip calculator")
bill = float(input("What was the total bill $ "))
tipAmount = int(input("What percentage tip would you like to give? 10, 12, or 15: "))
spiltBill = int(input("How many people to split the bill? "))

billWithTip = tipAmount / 100 * bill + bill / spiltBill
roundTotalAmount = "{:.2f}".format(billWithTip)
print(f"Each person pays $ {roundTotalAmount}")
