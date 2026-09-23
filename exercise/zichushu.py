def selfDividingNumbers(left: int, right: int):
  lists = []
  for zichushu in range(left, right+1):
      str_zichushu = str(zichushu)
      if str(0) in str_zichushu:
          continue
      else:
          for yiweishu in str_zichushu:
              if zichushu % int(yiweishu) != 0:
                  break
          else:
              lists.append(zichushu)
  print(lists)
  
selfDividingNumbers(1, 22)