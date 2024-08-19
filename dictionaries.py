# Dictionaries methods

stuff = {"food": 15, "energy": 100, "enemies": 3}

print(stuff.get("food"))

print(stuff.items())

print(stuff.keys())

print(stuff.popitem())
print(stuff)

print(stuff.setdefault("food"))
print(stuff)

print(stuff.setdefault("friends", 123))
print(stuff)

new_items = {"rocks": 4, "arrows": 18}
stuff.update(new_items)
print(stuff)

new_items = {"rocks": 2, "arrows": 5}
stuff.update(new_items)
print(stuff)

stuff.update(food = 500)
print(stuff)