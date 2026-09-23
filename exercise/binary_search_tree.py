from io import StringIO
import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        #Write your code here
        if root is None:
            return -1
        else:
            return max(self.getHeight(root.left), self.getHeight(root.right)) + 1

    def levelOrder(self,root):
        #Write your code here
        if root is not None:
            queue = [root]

        for node in queue:
            print(node.data,end=" ")
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)


sys.stdin = StringIO("""
7
3
5
2
1
4
6
7
""".strip())
                
T=int(sys.stdin.readline().strip())
myTree=Solution()
root=None
for i in range(T):
    data=int(sys.stdin.readline().strip())
    root=myTree.insert(root,data)
# height=myTree.getHeight(root)
# print(height) 
myTree.levelOrder(root)      