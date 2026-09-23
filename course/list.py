lists = [x for x in range(1, 5)]

# 1. Sum Items in List
print(sum(lists))

# 2. Multiply Items in List
result = 1
for i in lists:
    result *= i
print(result)

# 3. Get Largest Number in List
print(max(lists))

# 4. Get Smallest Number in List
print(min(lists))

# 5. Count Strings with Same Start and End
count = 0
for i in ['abc', 'xyz', 'aba', '1221']:
    if i[0] == i[-1]:
        count += 1
print(count)

# 6. Sort Tuples by Last Element
print(sorted([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)], key=lambda x:x[1]))

# 7. Remove Duplicates from List
lists = ['abc', 'xyz', 'abc', 'abc']
for x in lists:
    if lists.count(x) != 1: 
        lists.remove(x)
print(lists)