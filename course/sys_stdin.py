import sys
from io import StringIO

sys.stdin = StringIO("""
2
Tom 123
Jerry 456
Tom
Bob
""".strip())

n = int(sys.stdin.readline().strip())
phone_book = {}
for _ in range(n):
    name, num = sys.stdin.readline().split()
    phone_book[name] = num

for line in sys.stdin:
    line = line.strip()
    if line in phone_book:
        print(f"{line}={phone_book[line]}")
    else:
        print("Not found")