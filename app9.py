# List functions

lucky_numbers = [42, 23, 15, 16, 8, 4]
friends = ["Kevin", "karen", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(1, "Kelly")
friends.remove("Jim")
print(friends)

friends.pop()
print(friends)

print(friends.index("Oscar"))
print(friends.count("Oscar"))

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)

friends.clear()
print(friends)
