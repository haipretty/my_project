
import re

# 用一个带分组的正则来演示
pattern = re.compile(r'(\d{4})-(\d{2})-(\d{2})')
text = "今天是 2026-06-19，明天是 2026-06-20"
match = pattern.search(text)

print("=== 匹配对象 ===")
print(f"match 对象: {match}\n")

print("=== group() / group(0) ===")
print(f"match.group()     = '{match.group()}'")
print(f"match.group(0)    = '{match.group(0)}'")
print("→ 返回整个匹配的字符串（所有分组加起来的完整匹配）\n")

print("=== group(n) 第 n 个分组 ===")
# 典型用途：提取结构化数据，比如从日期字符串中分别取出年、月、日
print(f"match.group(1)    = '{match.group(1)}'")  # 年份
print(f"match.group(2)    = '{match.group(2)}'")  # 月份
print(f"match.group(3)    = '{match.group(3)}'")  # 日期
print("→ 按括号顺序，返回第 n 个分组的内容\n")

print("=== group('name') 通过名字获取分组内容 ===")
# 用命名分组提取年、月、日
pattern2 = re.compile(r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})')
match2 = pattern2.search(text)

print(match2.group('year'))   # 2026
print(match2.group('month'))  # 06
print(match2.group('day'))    # 19

print("=== groups() 所有分组 ===")
# 方便用元组解包：year, month, day = match.groups()
print(f"match.groups()    = {match.groups()}")
print("→ 返回一个包含所有分组的内容的元组\n")

print("=== start() / end() / span() ===")
print(f"match.start()     = {match.start()}")     # 整个匹配的起始位置
print(f"match.end()       = {match.end()}")       # 整个匹配的结束位置（不含）
print(f"match.span()      = {match.span()}\n")    # 整个匹配的位置区间(start, end)

print("=== 各分组的 start() / end() / span() ===")
print(f"match.start(1)    = {match.start(1)}, match.end(1) = {match.end(1)}, span(1) = {match.span(1)}")  # 第1分组
print(f"match.start(2)    = {match.start(2)}, match.end(2) = {match.end(2)}, span(2) = {match.span(2)}")  # 第2分组
print(f"match.start(3)    = {match.start(3)}, match.end(3) = {match.end(3)}, span(3) = {match.span(3)}")  # 第3分组
print("→ 传入 n 表示第 n 个分组的位置，不传表示整个匹配")
