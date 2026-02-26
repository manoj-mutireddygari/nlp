#global List
users = ["admin","guest","guest","user"]
def rim1():
    new_users = []
    for u in users:
        if u != "guest":
            new_users.append(u)
    print("new_users:", new_users)

def rim2():
    for u in users[:]:
        if u == "guest":
            users.remove(u)
    print("users:", users)

rim1()
rim2()