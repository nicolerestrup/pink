tip_debt = int(input("A tips for a tip! Write your total debt. "))
if tip_debt > 100:
    over = tip_debt * 0.05
    print("Your tips for a tip is {}".format(over))
elif tip_debt <= 100:
    below = tip_debt * 0.1
    print("Your tips for a tip is {}".format(below))
else:
    print("This is not a number. Run the script again to give it another shot!")
