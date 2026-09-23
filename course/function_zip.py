from io import StringIO
import sys

sys.stdin = StringIO("""
5 3
89 90 78 93 80
90 91 85 88 86  
91 92 83 89 90.5
""".strip())


courses, students = sys.stdin.readline().split()
lists = []
for _ in range(int(students)):
    lists.append(list(sys.stdin.readline().split()))    #每个学生的成绩

print(lists)
scores = list(zip(*lists))                              #转换成每一课的成绩, *lists表示开一维
print(zip(*lists))
for score in scores:
    score = list(map(float, score))
    print(f"{sum(score)/len(score):.1f}")

