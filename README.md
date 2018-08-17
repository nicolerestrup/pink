# Hello
My name is Nicole and I like:
1. cats
2. music
3. technology
4. ~~going on walks~~ 

## And this is not any file
not any file that you've might expected

*A file with no information* that you actually need

**BOOOOOOM**

| What            | Cool  | Satus          |
| --------------- |:-----:| -------------: |
|Pink programming | 100%  | Already super! |
|Python camp      | 100%  | Already super! |
|My Python skills | 20%   | On it's way!   |


```python
hobbies = []
answer = ""
while answer != "stop":
    answer = input("What's your hobbies? Write one at a time.")
    hobbies.append(answer)
hobbies.remove("stop")
reply = "Your hobbies are: {}"
print(reply.format(", ".join(hobbies)))
