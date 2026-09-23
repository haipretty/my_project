#1. Sort Dictionary by Value
dicts = {"color":"3", "type":"2", "model":"1"}
print(dicts)
newDict = dict(sorted(dicts.items(), key=lambda x:x[1]))
print(newDict)
#newDict2 = dict(sorted(dicts, key=lambda x:dicts[x])) #dicts iterate后只剩keys
#print(newDict2)

#2. Add Key to Dictionary
dicts = {0: 10, 1: 20}
dicts[2] = 30
print(dicts)

#3. Concatenate Dictionaries
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dicts = dic1.copy()
dicts.update(dic2)      #在dicts上更新
dicts.update(dic3)
print(dicts)

#4. Check Key Existence in Dictionary
if 3 in dic1:
    print(True)
else:
    print(False)

#5. Iterate Over Dictionary Using For Loops
for x,y in dic1.items():
    print(x,":",y)

i = 1
print(-i)