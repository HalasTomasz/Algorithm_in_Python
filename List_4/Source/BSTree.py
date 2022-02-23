class BSTNode:
    
    comparing = 0
    size = 0
    Msize = 0
    
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value
        self.parent = None

        
    def pre_insert(self, value):
        BSTNode.size +=1
        if BSTNode.size > BSTNode.Msize:
            BSTNode.Msize = BSTNode.size 
        self.insert(value)
        
    def Insert(self, value):
  
        if not self.value:
            self.value = value
            return

        BSTNode.comparing +=1
        if value < self.value:
            if self.left:
                self.left.Insert(value)
                return
            self.left = BSTNode(value)
            return

        if self.right:
            self.right.Insert(value)
            return
        self.right = BSTNode(value)


    def Min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.value

    def Max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.value
    
    def pre_delete(self, value):
        if self.Find(value) == 1:
            BSTNode.size -=1
            self.Delete(value)
        else: 
            return    
   
        
    def Delete(self, value):
        if self == None:
            return self
        
        BSTNode.comparing +=1
        if value < self.value:
            if self.left:
                self.left = self.left.Delete(value)
            return self
        
        BSTNode.comparing +=1
        if value > self.value:
            if self.right:
                self.right = self.right.Delete(value)
            return self
        
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        
        success = self.right
        while success.left:
            success = success.left
        self.value = success.value
        self.right = self.right.Delete(success.value)
        return self

    def Find(self, value):
        
        BSTNode.comparing +=1
        if value == self.value:
            return 1
        
        BSTNode.comparing +=1
        if value < self.value:
            if self.left == None:
                return 0
            return self.left.Find(value)
        BSTNode.comparing +=1
        if self.right == None:
            return 0
        return self.right.Find(value)


    def inorder(self, arr):
        if self.left is not None:
            self.left.inorder(arr)
        if self.value is not None:
            arr.append(self.value)
        if self.right is not None:
            self.right.inorder(arr)
        return arr
    
    def Succesor(self,data):
        
        BSTNode.comparing +=1
        if self.value == data:  
             if self.right != None:
                 current = self.right
                 while current.left is not None:
                     current = current.left
                 return current.value
        
             if self.left != None:
                 return self.left.value
             
        BSTNode.comparing +=1   
        if data < self.value:
            if self.left == None:
                return 
            return self.left.Succesor(data)

        if self.right == None:
            return 
        return self.right.Succesor(data)


