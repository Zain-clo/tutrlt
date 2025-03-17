colors=["red","orange","yellow","green"]
print(colors[0])
print(colors[-1])

colors.remove("yellow")
print(colors)
colors.append("orange")
print(colors)
colors.pop()
print(colors)
colors.sort()
print(colors)
colors.reverse()
print(colors)


user1 = {
   "name": "Zaianb",
   "email": "me@gmail.com"
}
print(user1["name"])
print(user1.get("email"))

user1["email"] = "me@gmail.com"
print(user1)
user1.clear()
print(user1)

