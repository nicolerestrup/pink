word = input("Write a word that you want to translate to Rövarspråket\n")
cons = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
y = ("")
for x in word:
    if x in cons:
        y += (x + "o" + x)
    else:
        y += x
print(y)
