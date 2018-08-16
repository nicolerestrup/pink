def dl_to_cup(dl):
    return  "{} dl is {} cups".format(dl, dl / 2.37)
#cal = answer * dl_in_cup
answer = int(input("Write your number in deciliters that you want to convert to cups."))
print(dl_to_cup(answer))
