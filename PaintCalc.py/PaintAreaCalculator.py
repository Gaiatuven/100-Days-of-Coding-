def paint_calc(height, width, cover):
    number_of_cans = (test_h * test_w) / coverage
    roundNumberOfCans = round(number_of_cans, 0)
    print(roundNumberOfCans)

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
