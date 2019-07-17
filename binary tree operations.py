class Node:
    a = []
    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def printtree(self):
        if self.left:
            self.left.printtree()
        Node.a.append(self.data)
        if self.right:
            self.right.printtree()

    def insert(self, data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
            
    def search(self, data):
        if data:
            if data==self.data:
                return "found"
            elif data<self.data:
                if self.left is not None:
                    self.left.search(data)
            elif data>self.data:
                if self.right is not None:
                    self.right.search(data)
            else:
                return "not found"


l = int(input())
n = [int(x) for x in input().split()]
root = Node(n[0])
for i in range(1,l):
    root.insert(n[i])
root.printtree()
print(root.a)
print(root.search(int(input("search element:"))))
