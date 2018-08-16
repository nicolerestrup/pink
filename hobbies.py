hobbies = []
answer = ""
while answer != "stop":
    answer = input("What's your hobbies? Write one at a time.")
    hobbies.append(answer)
hobbies.remove("stop")
reply = "Your hobbies are: {}"
print(reply.format(", ".join(hobbies)))
