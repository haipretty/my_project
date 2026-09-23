
import sys
from io import StringIO
import math
import random
from datetime import datetime
import re
from itertools import combinations,permutations
# import numpy as np

#===== 第一题：三位数 =====
# digit = [1, 2, 3, 4]
# result = []
# for i in digit:
#     for j in digit:
#         if i == j:
#             continue
#         else:
#             for k in digit:
#                 if i == k or j == k:
#                     continue
#                 else:
#                     result.append(i*100+j*10+k)
# print(result)
# print(len(result))

#===== 第二题：遍历 =====
# list = []
# for num in range(2000, 3201):
#     if num % 7 == 0 and num % 5 != 0:
#         list.append(num)
# print(list)

# sys.stdin = StringIO("""

# """.strip())
# sys.stdin.readline()

#===== 第三题：排序 =====
# x = input("请输入第一个整数x：")
# y = input("请输入第二个整数y：")
# z = input("请输入第三个整数z：")

# list = [x, y, z]
# list.sort()                         #列表方法 
# print(sorted(list))                 #可迭代对象排序

#===== 第四题：判断字符 =====
# str = input("请输入字符：")
# dict  = {
#     "yingwen": 0,
#     "kongge": 0,
#     "shuzi": 0,
#     "qita": 0
# }
# for s in str:
#     if s.isalpha():               #字母
#         dict["yingwen"] += 1
#     elif s.isdigit():             #数字
#         dict["shuzi"] += 1
#     elif s.isspace():             #空格
#         dict["kongge"] += 1
#     else:
#         dict["qita"] += 1
# print(dict) 

#===== 第五题：阶乘和 =====
# def sum_factorial(n: int) -> int:
#     total = 0
#     for i in range(1, n+1):
#         total += math.factorial(i)    #阶乘
#     return total

# print(sum_factorial(20))

#===== 第六题：递归 =====
# def print_reverse(str, index):
#     if index >= len(str):             #1.跳出条件
#         return
    
#     print_reverse(str, index+1)       #2.升级
#     print(str[index])

# print_reverse("abcdefg", 0)

#===== 第七题：回文数 =====
# def huiwenshu(num: str) -> bool:
#     return (num.isdigit() 
#             and len(num) == 5 
#             and num[0] != "0" 
#             and num == num[::-1]          #字符串倒序
#     )

# num = input("请输入数字：").strip()
# if huiwenshu(num):
#     print(f"{num}是回文数")
# else:
#     print(f"{num}不是回文数")

#===== 第八题：分类 =====
# score = float(input("输入成绩："))
# grade = "A" if score >= 90 else (           #条件嵌套
#     "B" if 60 <= score <= 89 else "C")
# print(grade)

#===== 第九题：温度转换器 =====
#公式：C = (F-32)*5/9
# def fahrenheit_to_celsius(fahrenheit):
#     celsius = (fahrenheit-32)*5/9
#     return celsius

#===== 第10题：闰年判断 =====
# def is_leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False

# if __name__ == "__main__":
#     try:
#         print(is_leap_year(2304))
#     except Exception as e:
#         print(e)

#===== 第11题：递归阶乘 =====
# def jiecheng(num):
#     if num == 0:                          #1.跳出条件
#         return 1
#     else:
#         return num*jiecheng(num-1)        #2.降级

#===== 第12题：递归年龄 =====
# def age(person_no):
#     if person_no == 1:
#         return 10
#     else:
#         return 2+age(person_no-1)

# print(age(5))

#===== 第13题：数字位数及倒序打印 =====
# def main():
#     try:
#         num = input("请输入不多于5位的正整数：")
#         int(num)
#     except ValueError:
#         print("请输入有效数字")
#         return
    
#     print(f"{num}的位数是{len(num)}")
#     print(f"{num}倒序{num[::-1]}")              
#     print(f"{num}倒序{"".join(reversed(num))}")     #可迭代对象倒序+连接

# main()

#===== 第14题：冒泡排序 =====
# def bubble_sort(nums):
#     n = len(nums)
#     for i in range(0, n-1):
#         for j in range(i+1, n):                         #先排小的
#             if nums[i] > nums[j]:
#                 nums[i], nums[j] = nums[j], nums[i]     #变量互换
#     return nums

# def bubble_sort2(nums):
#     n = len(nums)
#     for i in range(n-1):
#         for j in range(0, n-1-i):                       #先排大的
#             if nums[j] > nums[j+1]:
#                 nums[j], nums[j+1] = nums[j+1], nums[j]
#     return nums

# print(bubble_sort([2,3,1,5,4]))
# print(bubble_sort2([2,3,1,5,4]))

#===== 第15题：有序插入 =====
# a = [1,4,6,9,13,16,19,28,40,100]
# num = int(input("请输入一个数："))
# index = 0
# for i in a:
#     if num <= i:
#         break
#     else:
#         index += 1
# a.insert(index, num)                    #列表插入
# print(a)

#===== 第16题：数组逆序 =====

#===== 第17题：矩阵相加 =====
# x = [[12,7,3],
#     [4,5,6],
#     [7,8,9]]
# y = [[5,8,1],
#     [6,7,3],
#     [4,5,9]]
# # X = np.array(x)      #利用numpy
# # Y = np.array(y)
# # print(X+Y)

# z = [[],[],[]]
# for i in range(len(x)):                 #len(二维list)=行数
#     for j in range(len(x[0])):
#         z[i].append(x[i][j]+y[i][j])
# print(z)

#===== 第18题：数字平方 =====
# try:
#     num = int(input("请输入数字："))
#     if num**2 < 50:
#         print(f"{num} 的平方小于50")
#     else:
#         print(f"{num} 的平方大于等于50")
# except Exception as e:
#     print(e)

#===== 第19题：随机数的平方 =====
# random.seed(2026)
# num = random.randint(1, 100)
# print(f"{num} 的平方是 {num**2}")

#===== 第20题：列表排序与连接 =====
# a = [1,3,2]
# b = [4,3,5]
# a.sort()                            
# b.sort()
# print(a,"\n",b)
# print(a+b)
# a.extend(b)                                       #扩展list
# print(a)

#===== 第21题：找年龄最大的人 =====
# person = {
#     "li": 18,
#     "wang": 50, 
#     "zhang": 20,
#     "sun": 22
#     }
# max_name = max(person, key=person.get)              #带key方法的max
# max_name = max(person, key=lambda x: person.get(x))
# print(f"年龄最大的人是 {max_name}，年龄是 {person.get(max_name)}")

#===== 第22题：字符串排序 =====
# str = input("请输入字符串：")
# sorted_list = sorted(str)
# sorted_str = "".join(sorted_list)
# print(sorted_str)

#===== 第23题：子串出现的次数 =====
# str = input("请输入字符串：")
# sub_str = input("请输入要查找的字符：")
# count = str.count(sub_str)                  #子串个数
# print(count)

#===== 第24题：输入字符，逐个写入磁盘 =====
# with open("temp.txt", "w") as f:
#     while True:
#         char = sys.stdin.read(1)            #读取一个字符
#         if char != "#":                     #遇到#号，停止写入
#             f.write(char)
#         else:
#             break

#===== 第25题：密码游戏 =====
# def decrypt(num):
#     num_str = str(num)
#     if len(num_str) != 4:
#         num_str = num_str.zfill(4)        #数字型字符串左侧补0
#     new_num = []
#     for s in num_str:
#         num = int(s)
#         num = (num + 3) % 9
#         new_num.append(num)
#     new_num[0], new_num[2] = new_num[2], new_num[0]
#     new_num[1], new_num[3] = new_num[3], new_num[1]
#     return 1000*new_num[0]+100*new_num[1]+10*new_num[2]+new_num[3]

# print(decrypt(123))

#===== 第26题：九九乘法表 =====
# def multiply_form(n):
#     form = [""]*n
#     for row in range(1, n+1):
#         for col in range(1, row+1):
#             str = f"{row}*{col}={row*col} "
#             form[row-1] += str
#         form[row-1] = form[row-1].strip()
#     return form

# n = int(input("请输入行数："))
# form = multiply_form(n)
# for i in form:
#     print(i)

#===== 第27题：判断素数 =====
# def is_sushu(n):
#     if n <= 1:
#         return False        #1不是素数
#     elif n != 2 and n % 2 == 0:
#         return False        #除2以外的偶数都不是素数
    
#     for i in range(3, int(math.sqrt(n))+1, 2):  #从3开始到平方根，跳过偶数
#         if n % i == 0:
#             return False
        
#     return True

# print(is_sushu(5))

#===== 第28题：报数游戏 =====
# def count_num(n, m):
#     people = list(range(1, n+1))
#     index = 0
#     left = 0

#     while people:
#         index = (index + 2) % len(people)   #过两个位置出1人
#         person = people.pop(index)
#         left += 1
#         if person == m:
#             return left

# print(count_num(10,4))          #4是留到最后的人

#===== 第29题：查字典 =====
# fruit = ['apple', 'banana','strawberry', 'orange', 'mango', 'grape', 'blueberry']
# number = [1, 3, 5, 6, 13, 21, 10]
# fruit_dict = dict(zip(fruit, number))                   #dict(zip())创建字典

# name = input("请输入水果：")
# print(f"水果 {name} 有 {fruit_dict.get(name, 0)} 个")

# # %%
#===== 第30题：字母出现次数 =====
# def char_count(str):
#     dict = {}
#     for char in str:
#         dict[char] = dict.get(char, 0) + 1              #dict.get()设置默认值
#     return dict

# string = input("请输入字符串：")
# print(char_count(string))

#===== 第31题：元组的操作 =====
# base_list = [3,6,9,0,5,8]
# tpl = tuple(base_list)
# half_index = len(tpl)//2                                    #整除
# print(tpl[half_index:])                                     #元组切片

# n = int(input("请输入一个数字："))
# print(f"{n}是否在元组中 {n in tpl}")

# if n not in tpl:
#     tpl += (n,)*3
# print(f"{tpl} 长度是 {len(tpl)}")

#===== 第32题：打印菱形图案 =====
# def print_diamond(n1, n2, c):
#     if 0 < c < 4:
#         print(" "*n1+"#"*n2)                #分别打印空格数量和#号数量
#         print_diamond(n1-1, n2+2, c+1)
#     elif 4 <= c <= 7:
#         print(" "*n1+"#"*n2)
#         print_diamond(n1+1, n2-2, c+1)
#     else:
#         return

# print_diamond(4, 1, 1)

#===== 第33题：日期计算 =====
# def count_day(date1, date2):
#     date1 = datetime.strptime(date1, "%Y%m%d %H:%M:%S")       #datetime：解析日期
#     date2 = datetime.strptime(date2, "%Y%m%d %H:%M:%S")
#     print(date1.strftime("%Y-%m-%d %H:%M:%S"))                #格式化输出
#     print(date2.strftime("%Y-%m-%d %H:%M:%S"))
#     diff = date2 - date1                                      #相减，返回timedelta
#     return diff.days                                          #取天数

# date1 = input("请输入生日：")
# date2 = input("请输入当前日期：")
# print(f"{count_day(date1, date2)} 天")

#===== 第34题：图形面积 =====
# class Square:                                           #父类  
#     def __init__(self, width:int) -> None:              #方法说明：参数类型+返回值类型
#         self.width = width

#     def area(self) -> float:
#         return float(self.width ** 2)

# class Rectangle(Square):                                #子类
#     def __init__(self, width:int, height:int) -> None:
#         self.width = width
#         self.height = height

#     def area(self) -> float:
#         return float(self.width * self.height)

# class Circular(Square):
#     def area(self) -> float:
#         return math.pi * (self.width ** 2)

# class Triangle(Square):
#     def area(self) -> float:
#         return math.sqrt(3) * (self.width**2) / 4

# category = input("请输入图形种类：")
# if category == "Square":
#     width = int(input("请输入边长："))
#     area = Square(width).area()
#     print(f"{category} 的面积是 {area}")
# elif category == "Rectangle":
#     width, height = map(int, input("请输入边宽和边长：").split(" "))
#     area = Rectangle(width, height).area()
#     print(f"{category} 的面积是 {area}")
# elif category == "Circular":
#     width = int(input("请输入半径："))
#     area = Circular(width).area()
#     print(f"{category} 的面积是 {area:.3f}")
# elif category == "Triangle":
#     width = int(input("请输入边长："))
#     area = Triangle(width).area()
#     print(f"{category} 的面积是 {area:.3f}")

#===== 第35题：提取字符串 =====
# num = input("请输入电话号码：")
# pattern = re.compile(r"\d+(?:-\d+)*")               #(?:)非分组
# match = pattern.search(num)
# phone_num = match.group()
# digits = phone_num.replace("-", "")                 #字符串替换

# print(phone_num)
# print(digits)

#===== 第36题：IP地址 =====
# def check_ip(ip):
#     pattern = r"^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}$"
#     match = re.match(pattern, ip)
#     try:
#         print(match.group())                         #正则表达式：^$开头结尾，\.匹配点
#     except Exception:
#         print("未匹配到！")
#     if match:
#         print("legal")
#     else:
#         print("illegal")

# while True:
#     ip = input("请输入IP地址：")
#     if ip == "#":
#         break
#     else:
#         check_ip(ip)

#===== 第37题：字符串查找 =====
# def find_char(str_a, str_b):
#     return str_b.find(str_a)                        #字符串查找，失败返回-1

# str_a = "World"
# str_b = "Hello World"
# print(find_char(str_a, str_b))
# print(str_b.rindex(str_a))                          #字符串右索引位，失败报错

#===== 第38题：字符串去重 =====
# def remove_duplicate(string):
#     str_list = []
#     for s in string:
#         if s not in str_list:
#             str_list.append(s)
#     return "".join(str_list)

# print(remove_duplicate("aaasssccccdd"))

#===== 第39题：字符串去重后排序 =====
# def deduplicate_sort(string):
#     result = sorted(set(string))                    #用set去重，用sorted排序
#     return "".join(result)                          #连接成字符串

# print(deduplicate_sort("aaasssccccdd"))

#===== 第40题：切片取最大的三个数 =====
# numbers = [3,1,4,1,5,9,2,6,5,3,5]

# largest_three = sorted(numbers, reverse=True)[:3]       #sorted排序
# print(largest_three)

# numbers.sort(reverse=True)                              #列表sort排序
# largest_three2 = numbers[:3]
# print(largest_three2)

#===== 第41题：按字符串长度排序 =====
# def sort_by_length(str_list):
#     return sorted(str_list, key=len)                    #带key方法的sorted排序

# str_list = ["apple", "hi", "python", "a", "hello world", "code"]

# print(sort_by_length(str_list))

#===== 第42题：斐波那契数列 =====

#===== 第43题：复制列表 =====
# list = [1,2,3,4,5]
# list2 = list.copy()
# print(list)
# print(list2)

#===== 第44题：猜数字 =====
# num = random.randint(1, 100)
# while True:
#     guess = input("请输入数字：")
#     try:
#         guess = int(guess)
#         if guess < num:
#             print("您猜小了")
#         elif guess > num:
#             print("您猜大了")
#         else:
#             print("恭喜~ 您猜对了！")
#             break
#     except Exception:
#         pass

#===== 第45题：最长公共前缀 =====
# strs = ["abca", "abc", "abca", "abc", "abcc"]
# common_str = strs[0]
# common_str_len = len(strs[0])
# for str in strs[1:]:
#     str_len = len(str)
#     min_index = min(common_str_len, str_len)
#     count = 0
#     for c, s in zip(common_str[:min_index], str[:min_index]):
#         if c == s:
#             count += 1
#         else:
#             break
#     common_str = common_str[:count]
#     common_str_len = count

# print(strs)
# print(common_str)

# str.startswith(s)                     #字符串开头

#===== 第46题：判断字符是否唯一 =====
# str = "abcdefg"
# str_set = set(str)
# str_len = len(str)
# set_len = len(str_set)
# print(f"字符串长度 {str_len}")
# print(f"集合长度 {set_len}")
# if str_len == set_len:
#     print("字符串中字符均不同")
# else:
#     print("字符串中有重复字符")

#===== 第47题：字符串变形 =====
# str = "Hello World"
# print(str)
# str_list = str.split()                          #字符串分割
# str_reverse = " ".join(str_list[::-1])          #列表倒序+连接
# str_revert_capital = "".join([s.upper() if s.islower() else s.lower() for s in str_reverse])

# # str_revert_capital = ""
# # for s in str_reverse:
# #     if s and s.islower():
# #         str_revert_capital += s.upper()
# #     elif s and s.isupper():
# #         str_revert_capital += s.lower()
# #     else:
# #         str_revert_capital += s

# print(str_revert_capital)

#===== 第48题：压缩字符串 =====
# def compress_str(string:str)->str:
#     if len(string) <= 1:
#         return string
        
#     string_new = string[0]
#     count = 1
#     for s in string[1:]:
#         if string_new[-1] == s:
#             count += 1
#         else:
#             if count >= 2:
#                 string_new += str(count)
#             string_new += s
#             count = 1
#     if count >= 2:
#         string_new += str(count)
#     return string_new

# string = "aabcccccaaa"
# print(string)        
# print(compress_str(string))

#===== 第49题：选择排序 =====
# def choose_sort(nums:list)->None:
#     n = len(nums)
#     for i in range(n-1):
#         min_index = i                         #最小值索引位
#         for j in range(i+1, n):
#             if nums[j] < nums[min_index]:     #遍历后面的元素，逐个比较
#                 min_index = j                 #记新的最小值索引位
#         if min_index != i:
#             nums[min_index], nums[i] = nums[i], nums[min_index]   #互换

# nums = [7, 6, 5, 4, 3, 2, 1]
# choose_sort(nums)
# print(nums)

#===== 第50题：插入排序 =====
# def insert_sort(nums:list)->None:
#     n = len(nums)

#     for i in range(1, n):                 #[7, 8, 5, 4, 3, 2, 1]
#         sorting_num = nums[i]
#         j = i - 1

#         while j>=0 and nums[j] > sorting_num:
#             nums[j+1] = nums[j]           #一直往后挪
#             j -= 1

#         nums[j+1] = sorting_num           #补到j+1位

# nums = [7, 8, 5, 4, 3, 2, 1]
# insert_sort(nums)
# print(nums)

#===== 第51题：合并排序数组 =====
# def merge_sorted_list(nums1:list, nums2:list)->list:
#     merged_list = []
#     i = j = 0
#     while i < len(nums1) and j < len(nums2):
#         if nums1[i] <= nums2[j]:
#             merged_list.append(nums1[i])
#             i += 1
#         else:
#             merged_list.append(nums2[j])
#             j += 1
#     if i > len(nums1):
#         merged_list.extend(nums2[j:])
#     else:
#         merged_list.extend(nums1[i:])
#     return merged_list

# nums1 = [1, 2, 4, 5, 8]
# nums2 = [3,6,7]
# print(merge_sorted_list(nums1, nums2))

#===== 第52题：数位之和 =====
# def is_beauty_num(nums:list)->dict:
#     dict_nums = {}
#     for num in nums:
#         total = sum(int(i) for i in num)                      #sum函数+for：iter和
#         dict_nums[num] = "Yes" if total % 7 == 0 else "No"
#     return dict_nums

# n = int(input("正整数个数："))
# nums = []
# for _ in range(n):
#     nums.append(input())
# dict_nums = is_beauty_num(nums)
# print(dict_nums)

#===== 第53题：删除字符 =====
# string = "abcdedgfeadf"
# sub = "abc"
# sub_set = set(sub)
# print(string)
# removed_str = "".join(s for s in string if s not in sub_set)    #for+if推导式：从iter中取出=i的数
# print(removed_str)

#===== 第54题：目标移动 =====
# nums = [1,2,3,4,5,6]
# target = 3
# target_count = nums.count(target)                             #数个数
# target_list = [target]*target_count
# target_list = [num for num in nums if num == target]
# other_list = [num for num in nums if num != target]           #for+if推导式
# result = target_list + other_list
# print(result)

#===== 第55题：统计数字 =====
# def count_digit_occur(k:int, n:int)->int:
#     if k < 0  or k > 9:
#         raise ValueError("k必须是0~9的整数")
#     if n < 0:
#         raise ValueError("n必须是非负整数")
    
#     total = 0
#     total = sum(str(i).count(str(k)) for i in range(n+1))
#     return total

# print(count_digit_occur(4, 20))

#===== 第56题：手机号马赛克 =====
# def mask_phone(phone:str)->str:
#     if len(phone) != 11:
#         return ""
    
#     new_phone = phone[:3] + "****" + phone[-4:]
#     return new_phone

# print(mask_phone("13211111111"))

#===== 第57题：计算大小写字母 =====

#===== 第58题：元组排序 =====
# """
# Tom,19,80;John,20,90;Jony,17,91;Jony,17,93; Json, 21,85
# """
# string = input("请输入元组：")

# tuple_list = [tuple(map(lambda s: s.strip(), str.split(","))) for str in string.split(";")]

# sorted_tuple = sorted(tuple_list, key=lambda x: (x[0], x[1], x[2]))         #带key的sorted函数，指定多个排序项

# print(sorted_tuple)

#===== 第59题：创建字典 =====
# def print_square_dict():
#     dict = {}
#     for i in range(1, 4):
#         dict[i] = i**2
#     print(dict)

# print_square_dict()

#===== 第60题：邮箱切割 =====
# def extract_username(email:str)->str:
#     username = email.split("@")[0]
#     return username

# print(extract_username("john@google.com"))

#===== 第61题：编码与解码 =====
# text = "Hello, 世界！"

# #utf-8编码
# encode_utf8 = text.encode("utf-8")
# print("UTF-8编码", encode_utf8)
# decode_utf8 = encode_utf8.decode("utf-8")
# print("UTF-8解码", decode_utf8)

# #GBK编码
# text2 = "Hello, 世界！"
# encode_gbk = text2.encode("gbk")
# print("GBK编码", encode_gbk)
# decode_gbk = encode_gbk.decode("gbk")
# print("GBK解码", decode_gbk)

#===== 第62题：大象喝水 =====
# math.ceil()                     #向上取整

#===== 第63题：高空抛物 =====
# def distance(h:int, n:int)->float:
#     height = h
#     distance = 0
#     for i in range(1,n+1):
#         distance += height
#         if i != 1:
#             distance += height       
#         height /= 2
#     return distance

# print(distance(10, 3))

#===== 第64题：这一天是否存在 =====
# def is_leap_year(year:int)->bool:
#     return (year % 4 == 0 and year % 100 != 0) or (year % 400) == 0

# def is_date_exists(date:str)->bool:
#     if len(date) != 8 or not date.isdigit():
#         return False
    
#     year = int(date[:4])
#     month = int(date[4:6])
#     day = int(date[6:])
   
    # if day == 31:
    #     if month in (2, 4, 6, 9, 11):
    #         return False
    # elif day == 30:
    #     if month == 2:
    #         return False
    # elif day == 29 and month == 2:
    #     if not is_leap_year(year):
    #         return False
    # return True

    # month_days = {
    #     #31天
    #     1:31,3:31,5:31,7:31,8:31,10:31,12:31,
    #     #30天
    #     4:30,6:30,9:30,11:30,
    #     #29/28天
    #     2: 29 if is_leap_year(year) else 28
    # }
 
    # return 1 <= day <= month_days[month]

#===== 第65题：一年中的第几天 =====
# def is_leap_year(year:int)->bool:
#     return (year % 4 == 0 and year % 100 != 0) or (year % 400) == 0

# def days(date:str)->int:
#     if len(date) != 8 or not date.isdigit():
#         return False
    
#     year = int(date[:4])
#     month = int(date[4:6])
#     day = int(date[6:])

#     month_days = [31,28+is_leap_year(year),31,30,31,30,31,31,30,31,30,31]
#     return sum(month_days[:month-1])+day

# print(days("20260412"))

#===== 第66题：评委打分 =====
# n = int(input("请输入个数："))
# scores = []
# for _ in range(n):
#     scores.append(int(input()))

# # scores.pop(scores.index(max(scores)))     #pop：按index移除
# # scores.pop(scores.index(min(scores)))
# scores.remove(max(scores))                  #remove：按value移除
# scores.remove(min(scores))

# score = math.ceil(sum(scores)/len(scores))
# print("总分是：",score)

#===== 第67题：自行车骑行 =====
#自行车：上车27s，下车23s，3m/s
#步行：1.2m/s

# def choose_vahicle(distance:int)->str:
#     bike = distance/3 + 27 + 23
#     walk = distance/1.2
#     return "bike" if bike < walk else ("walk" if walk < bike else "All")
# try:
#     distance = int(input("请输入距离：").strip())
# except (ValueError, EOFError) as e:                   #一次捕获多个异常

# print(choose_vahicle(distance))

#===== 第68题：计算邮资 =====
#weight <= 1000g fare = 8元
#weight - 1000g 每500g 4元
#urgent + 5元

# def calculate_postage(x, c):
#     postage = 8
#     if x > 1000:
#         postage += math.ceil((x - 1000) / 500) * 4

#     postage += 5 if c == "y" else 0

#     return postage

# x, c = input().split()
# print(calculate_postage(int(x), c))

#===== 第69题：等差数列 =====
# a1, a2, n = map(int, input().split())
# interval = a2 - a1
# an = a1 + (n-1) * interval
# print(an)

#===== 第70题：角谷猜想 =====
# def jiaogu(n):
#     if n == 1:
#         print("End")
#         return
#     elif n % 2 == 0:
#         next_n = n // 2                 #单斜杠除/，返回float
#         print(f"{n} / 2 = {next_n}")
#         return jiaogu(next_n)
#     else:
#         next_n = n * 3 + 1
#         print(f"{n} * 3 + 1 = {next_n}")
#         return jiaogu(next_n)

# n = int(input())
# jiaogu(n)

#===== 第71题：龟兔赛跑 =====
# x, y, t = map(int, input().split())
# # turtle = x * t + x * t1
# # rabbit = y * t1
# t1 = (x * t) // (y - x)
# max_distance = y * t1
# print(max_distance)

#===== 第72题：密码验证 =====
# def is_valid_password(password):
#     #条件1
#     length = len(password)
#     if length < 6 or length >12:
#         return False
    
#     #条件2
#     valid_char = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$")
#     if not all(p in valid_char for p in password):              #all函数：所有条件都是True
#         return False
    
#     #条件3
#     has_lower = any(p.islower() for p in password)              #any函数：任一条件是True
#     has_upper = any(p.isupper() for p in password)
#     has_digit = any(p.isdigit() for p in password)

#     if sum([has_lower, has_upper, has_digit]) < 2:
#         return False
    
#     #条件4
#     has_special = any(p in "!@#$" for p in password)
#     if not has_special:
#         return False
    
#     return True

# passwords = input().split(",")
# for password in passwords:
#     print(password, end=" ")
#     print("valid" if is_valid_password(password) else "invalid") 
        
#===== 第73题：高级回文数 =====
# def is_huiwenshu(num:str)->bool:
#     if not num.isdigit():
#         return False
    
#     reverse_num = num[::-1]
#     return num == reverse_num

# n = int(input("请输入整数："))
# count = 0
# for i in range(1, n+1):
#     i = str(i)
#     if len(i) == 1 or is_huiwenshu(i):
#         count = (count + 1) % 20091119
#         print(i, end=" ")
# print(count)

#===== 第74题：CPU核心数 =====
#性能核心p：至少1个，2个线程
#能效核心E：1个线程

# c, t = map(int, input().split())
# p = t - c
# e = 2 * c - t
# print(f"总核心数：{c}，总线程数：{t}")
# if p >= 1 and e >= 0:
#     print(f"性能核心数：{p}，能效核心数：{e}")
# else:
#     print("Error")

#===== 第75题：小杨报数 =====
# N = int(input().strip())
# M = int(input().strip())

# for i in range(1, N+1):
#     if i % M != 0:
#         print(i)

#===== 第76题：peter的烟 =====
# n, k = map(int, input().split())
# count = n
# if k > 1:
#     while n >= k:
#         n = n // k
#         count += n
# print(count)

#===== 第77题：欢乐的跳 =====
# def is_jolly(n:int, arr:list)->bool:
#     if n == 1:
#         return True
    
#     diffs = set()
#     for i in range(n-1):
#         diff = abs(arr[i+1] - arr[i])
#         diffs.add(diff)
#     required = set(range(1, n))
#     return diffs == required

# line = input().split()
# n = int(line[0])
# arr = list(map(int, line[1:]))
# print("Jolly" if is_jolly(n, arr) else "Not jolly")

#===== 第78题：排列组合 =====
# n, r = map(int, input().split())
# for comb in combinations(range(1, n+1), r):
#     print("".join(f"{x:>3}" for x in comb))         #占3个字符

#===== 第79题：三位数组合比例 =====
# for perm in permutations("123456789", 9):
#     a = int("".join(perm[:3]))
#     b = int("".join(perm[3:6]))
#     c = int("".join(perm[6:]))

#     if 3 * a == c and 2 * a == b:
#         print((a, b, c))

#===== 第80题：金字塔 =====
# n = int(input().strip())
# count = 0
# for i in range(1, n+1):
#     count += i * i
# #平方和公式：n(n+1)(2n+1)/6
# print(count)

#===== 第81题：BMI指数 =====
# m, h = map(float, input().split())
# bmi = m / (h ** 2)
# print("Underweight" if bmi < 18.5 else ("Normal" if 18.5 <= bmi < 24 else "Overweight"))

#===== 第82题：分类平均数 =====
# n, k = map(int, input().strip().split())
# k_times = []
# not_k_times = []
# for i in range(1, n+1):
#     if i % k == 0:
#         k_times.append(i)
#     else:
#         not_k_times.append(i)
# k_times_mean = sum(k_times) / len(k_times)
# not_k_times_mean = sum(not_k_times) / len(not_k_times)
# print(f"A类平均值：{k_times_mean:.1f}，B类平均值：{not_k_times_mean:.1f}")

#===== 第83题：极差 =====
# n = int(input().strip())
# nums = list(map(int, input().strip().split()))
# print(max(nums) - min(nums))

#===== 第84题：第2025个质数 =====
# def is_prime(n:int)->bool:
#     if n <= 1:
#         return False
#     if n != 2 and n % 2 == 0:
#         return False
#     for i in range(3, int(math.sqrt(n))+1, 2):
#         if n % i == 0:
#             return False
#     return True

# count = 1
# num = 1
# while count < 2025:
#     num += 2    
#     if is_prime(num):
#         count += 1
# print(num)

#===== 第85题：数列求和 =====
# n = int(input().strip())
# result = n * 25 + sum(range(25))
# print(result)

#===== 第86题：四叶玫瑰数 =====
# N, M = map(int, input().strip().split())
# for num in range(N, M+1):
#     str_num = str(num)
#     if len(str_num) == 4:
#         result = sum(int(i) ** 4 for i in str_num)
#         if result == num:
#             print(num)

#===== 第87题：哥德巴赫猜想 =====
#哥德巴赫猜想：任一大于2的偶数都可以写成两个质数之和
# def is_prime(n:int)->bool:
#     if n <= 1:
#         return False
#     if n != 2 and n % 2 == 0:
#         return False
#     for i in range(3, int(math.sqrt(n))+1, 2):
#         if n % i == 0:
#             return False
#     return True

# N = int(input().strip())
# for num in range(4, N+1, 2):
#     if num == 4:
#         print("4 = 2 + 2")
#     else:
#         for i in range(3, num//2+1, 2):
#             if is_prime(i) and is_prime(num-i):
#                 print(f"{num} = {i} + {num-i}")
#                 break

#===== 第88题：最长连号的长度 =====
# n = int(input().strip())
# nums = list(map(int, input().strip().split()))
# max_length = count = 1
# for i in range(n-1):
#     if nums[i+1] - nums[i] == 1:
#         count += 1
#         if count > max_length:
#             max_length = count
#     else:
#         count = 1
# print(max_length)

