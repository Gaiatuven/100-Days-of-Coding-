total = 0

for num in range(1 , 101):

    if num % 3 and num % 5 == 0:
        print("FizzBuzz")

    elif num % 3 == 0:
        print("Fizz")

    elif num % 5 == 0:
        print("Buzz")

    total += num
    print(num)
