import random
def code():
    adj = ["dance", "walk", "sitting", "jumping", "picking"]
    sub = ["glas", "clock", "phone", "computer", "bed"]
    number = random.randint(0,100)
    sign = ["!", ".", "#", "%", "&", "/", "?"]

    adj_rand = adj[random.randint(0, len(adj) -1)]
    sub_rand = sub[random.randint(0, len(sub) -1)]
    sign_rand = sign[random.randint(0, len(sign) -1)]

    print(adj_rand + sub_rand + str(number) + sign_rand)


code()
