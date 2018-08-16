list = [4, 7, 4, 3, 9]
numb = int(input("Fråga "))
lengh=len(list)
for i in range(lengh):
    if list[i] == numb:
        print(i)
