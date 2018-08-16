answer = input("What animal is furry with pointy ears and has a tail?")
if answer == "cat" or answer.lower() == "cat":
    print("You've answered {}! That's correct!".format(answer))
elif answer == "dog" or answer.lower() == "dog":
    yesno = input("That's soooooo close! Do you want another clue?")
    if yesno == "yes":
        dog = input("What's the opposit of a dog?")
        if dog == "cat" or answer.lower() == "cat":
            print("You've answered {}! That's correct!".format(dog))
        else:
            lastclue = input("{} is not correct.. Do you want your last clue?".format(dog))
            if lastclue == "yes" or answer.lower() == "yes":
                iflastclue = input("It has 4 legs and is a very common pet")
                if iflastclue == "cat" or answer.lower() == "cat":
                    print("You've answered {}! That's correct!".format(answer))
                else:
                    print("{} is also wrong! It's hard to understand that you didn't get that it's a cat...".format(iflastclue))
            else:
                print("That's too bad. The correct answer was cat.")
else:
    pick = input("You've answered {} which is not correct :( Do you want to try again?".format(answer))
    if pick == "yes":
        answer2 = input("So you need another clue? It's not a dog but a ..?")
        if answer2 == "cat" or answer.lower() == "cat":
            print("2nd luck is a charm! {} is correct!".format(answer2))
        else:
            print("You guessed {} which is not correct eather. The correct answer is cat.".format(answer2))
    else:
            print("That's too bad :( The answer is a cat!")
