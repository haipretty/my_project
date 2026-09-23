def generate(numRows: int):
  lists = []
  for i in range(numRows):    #行数
      innerLists = [1]
      if i == 0:
          pass
      elif i == 1:
          innerLists.append(1)
      else:
          for j in range(1, i):      #列数
              innerLists.append(lists[i-1][j-1]+lists[i-1][j])
          innerLists.append(1)
      lists.append(innerLists)
  return lists

print(generate(3))