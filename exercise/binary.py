binary_n = bin(5)[2:]
max_ones = 0
count = 0
for i in binary_n:
    if i == '1':
        count += 1
        if max_ones < count:
            max_ones = count
    else:
        count = 0
print(max_ones)