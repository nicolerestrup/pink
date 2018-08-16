def fibonacci(variablefan):
    if variablefan == 0:
        return 0
    elif variablefan == 1:
        return 1
    else:
        return fibonacci(variablefan -1) + fibonacci(variablefan -2)
data = int(input ("What posision in fibonacci do you want to know? "))
variablefan = fibonacci(data)
print(variablefan)
