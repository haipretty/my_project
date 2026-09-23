
#lists = [x*2 for x in range(5)]
#print(lists)

x = int(input())
y = int(input())
z = int(input())
n = int(input())

#lists = [sublist for sublist in xx if sum(sublist) != n]
lists = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k) != n]
print(lists)

'''
lists = []
allLists = []
for i in range(x+1):
    for j in range(y+1):
        for z in range(z+1):
            allLists.append([i,j,z])
            if (i+j+z) != n:
                lists.append([i,j,z])
print(allLists)
print(lists)
'''

