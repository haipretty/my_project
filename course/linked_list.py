from io import StringIO
import sys

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 

class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
        #Complete this method
        node = Node(data)
        
        if head is None:
            head = node
        else:
            current = head
            while current.next:
                current = current.next
            current.next = node

        return head
    
    def removeDuplicates(self,head):
        #Write your code here
        start = head
        while start and start.next:
            if start.data == start.next.data:
                start.next = start.next.next
            else:
                start = start.next
        return head


sys.stdin = StringIO("""
4
2
3
4
1
""".strip())

mylist= Solution()
# print(sys.stdin.readline(), end="")
T=int(sys.stdin.readline())
# print(T)
head=None
for i in range(T):
    data=int(sys.stdin.readline())
    head=mylist.insert(head,data)    
mylist.display(head)