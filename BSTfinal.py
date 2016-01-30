class Node:

    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self,data):
        if data < self.data:
            if self.leftChild is None:  # if Lchild is NULL
                self.leftChild = Node(data)
            else:
                self.leftChild.insert(data)  # insert in left of Lchild
                
        else:
             
            if self.rightChild is None:
                    self.rightChild = Node(data)
            else:
                    self.rightChild.insert(data)

    def remove(self, data, parentNode):
        if self.data== None:
            return self.data
        elif data < self.data:
            if self.leftChild is not None:
                self.leftChild.remove(data,self)
        elif data > self.data:
            if self.rightChild is not None:
                self.rightChild.remove(data,self)
        else:
            if self.leftChild is not None and self.rightChild is not None:  # Nodes with 2 children
                self.data = self.rightChild.getMin()
                self.rightChild.remove(data,self)
                
            if parentNode.leftChild== self:
                if self.leftChild is not None:
                    tempNode = self.leftChild
                else:
                    tempNode = self.rightChild
                parentNode.leftChild = tempNode

            if parentNode.rightChild == self:
                if self.leftChild is not None:
                    tempNode = self.leftChild
                else:
                    tempNode = self.rightChild
                parentNode.rightChild = tempNode
                



    def getMin(self):
        if self.leftChild is None:
            return self.data
        else:
            self.leftChild.getMin()

    
    def getMax(self):
        if self.rightChild is None:
            return self.data
        else:
            self.rightChild.getMax()

    def traverse(self):
        if self.leftChild is not None:
            self.leftChild.traverse()

        print(self.data)

        if self.rightChild is not None:
            self.rightChild.traverse()

       



class BST:

    def __init__(self):
        self.rootNode = None

    def insert(self, data):
        if not self.rootNode: #if not any node in tree
            self.rootNode = Node(data)
        else:
            self.rootNode.insert(data)

    def remove(self, dataToRemove):
        if self.rootNode:
            return self.rootNode.remove(dataToRemove, None)
    def getMax(self):
        if self.rootNode:
            return self.rootNode.getMax()

    def getMin(self):
        if self.rootNode:
            return self.rootNode.getMin()

    def traverse(self):
        if self.rootNode:
            self.rootNode.traverse()


bst = BST()
bst.insert(12)
bst.insert(10)
bst.insert(-2)  
bst.insert(1)
bst.traverse()

bst.remove(-2)
bst.traverse()


            

        
        

            
