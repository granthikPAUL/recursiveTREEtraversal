class Node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
        
class btree:
    def __init__(self,data):
        self.root=Node(data)
        self.s=[]
    def printtree(self,traversal_type):
        if traversal_type=='preorder':
            print(self.preorder(self.root))
        elif traversal_type=='inorder':
            print(self.inorder(self.root))
        else:
            print(self.postorder(self.root))

    
    def preorder(self,start):
        if start is not None:
            self.s.append(start.value)
            self.preorder(start.left)
            self.preorder(start.right)
        return self.s
    def inorder(self,start):
        if start is not None:
            self.inorder(start.left)
            self.s.append(start.value)
            self.inorder(start.right)
        return self.s
    def postorder(self,start):
        if start is not None:
            self.postorder(start.left)
            self.postorder(start.right)
            self.s.append(start.value)
        return self.s


        
        
        
a=btree(1)
a.root.left=Node(2)
a.root.right=Node(3)
a.root.right.left=Node(6)
a.root.right.right=Node(7)
a.root.left.left=Node(4)
a.root.left.right=Node(5)
a.printtree('preorder')
