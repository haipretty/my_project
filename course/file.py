data = """人生如戏，
全看演戏，
abc，
123。"""

with open("text.txt", "w", encoding="UTF-8") as f:
#    for line in datas:
        f.write(data)

#3. Append Text and Display
#    f.write("\nabc")


# with (open("text.txt", encoding="UTF-8")) as f:

#1. Read Entire File
#    print(f.read())            #全部
#    print(f.read(3))           #3个字符
#    print(f.readline())        #一行
#    print(f.readline(3))       #3个字符，不是3行
#    print(f.readlines())       #全部行list

#2. Read First 10 Lines         #读多行要用循环
#    for _ in range(10):
#        print(f.readline())

#4. Read Last 2 Lines
#    lines = f.readlines()
#    for i in range(len(lines)-2, len(lines)):
#        print(lines[i], end="")

#5. File to List
#    lists = []
#    for line in f:
#        lists.append(line)
#    print(lists)
