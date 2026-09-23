# 1. Create a Set
sets = {"red", "green", "blue"}
print(sets)

# 2. Iterate Over Sets
for i in sets:
    print(i, end=" ")
print()

# 3. Add Member(s) to a Set
sets.add("yellow")
print(sets)

# 4. Remove Item(s) from a Given Set
sets.remove("red")
print(sets)

# 5. Remove an Item from a Set if Present
sets.discard("red")
print(sets)
