deci_amount = 1
dl_in_cup = deci_amount / 2.37
answer = int(input("Write your number in deciliters that you want to convert to cups."))
cal = answer * dl_in_cup
print("{} deciliters is {}".format(answer, round(cal, 2)))
