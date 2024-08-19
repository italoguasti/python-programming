# List methods

fruits = ["peaches", "pears", "apples"]
years = [3, "1998", 2.5, 987, "1994"]

print(fruits, years)

# Append

fruits.append("oranges")
print(fruits)

# Extend

fruits.extend(years)
print(fruits)

# Remove

fruits.remove("oranges")
print(fruits)

# Pop (remove from index)
fruits.pop(0)
print(fruits)

fruits.pop(-1)
print(fruits)

# Sort

numbers = [5, 1928, 4, 17, 68]
numbers.sort()
print(numbers)

# In
print("apple" in fruits)
print("apples" in fruits)

# Count
print(fruits.count("apples"))

# Index
print(fruits.index("apples"))