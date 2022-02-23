class Node:
    def __init__(self, data):
      self.left = None
      self.right = None
      self.parent = None
      self.data = data
      self.color = 1

class RedBlackTree:
    
    comparing = 0
    size = 0
    Msize = 0
    
    def __init__(self):
      nil_Node =  Node(-1)
      nil_Node.color = 0
      self.NIL = nil_Node
      self.root = self.NIL
    
    def left_rotate(self, x):
      y = x.right
      x.right = y.left
      
      if y.left != self.NIL:
        y.left.parent = x
      y.parent = x.parent
      
      if x.parent == self.NIL:
        self.root = y
      elif x == x.parent.left:
        x.parent.left = y
        
      else: 
        x.parent.right = y
      y.left = x
      x.parent = y
    
    def right_rotate(self, x):
      y = x.left
      x.left = y.right
      
      if y.right != self.NIL:
        y.right.parent = x
      y.parent = x.parent
      
      if x.parent == self.NIL: 
        self.root = y
      elif x == x.parent.right: 
        x.parent.right = y
      else:
        x.parent.left = y
      y.right = x
      x.parent = y
    
    
    def insert_fixup(self, node):
        
      while node.parent.color == 1:
          
        RedBlackTree.comparing +=1 
        if node.parent == node.parent.parent.left: 
          tmp = node.parent.parent.right 
              #Recolor
          if tmp.color == 1: 
            node.parent.color = 0
            tmp.color = 0
            node.parent.parent.color = 1
            node = node.parent.parent
            #Rotation
          else:
            RedBlackTree.comparing +=1 
            if node == node.parent.right:
              node = node.parent 
              self.left_rotate(node)
    
            node.parent.color = 0 
            node.parent.parent.color = 1
            self.right_rotate(node.parent.parent)
    
        else:
          tmp = node.parent.parent.left
              #Recolor
          if tmp.color == 1:
            node.parent.color = 0
            tmp.color = 0
            node.parent.parent.color = 1
            node = node.parent.parent
            #Rotation
          else:
            RedBlackTree.comparing +=1 
            if node == node.parent.left:
              node = node.parent 
              self.right_rotate(node)
    
            node.parent.color = 0 
            node.parent.parent.color = 1
            self.left_rotate(node.parent.parent)
    
      self.root.color = 0
    
    def pre_insert(self,value):
        RedBlackTree.size +=1
        if RedBlackTree.size > RedBlackTree.Msize:
            RedBlackTree.Msize = RedBlackTree.size 
        self.Insert(value)
    
    def Insert(self, value):
        
      newNode= Node(value)
      y = self.NIL
      temp = self.root
    
      while temp != self.NIL:
        y = temp
        RedBlackTree.comparing +=1 
        if newNode.data < temp.data:
          temp = temp.left
        else:
          temp = temp.right
    
      newNode.parent = y
      RedBlackTree.comparing +=1 
      if y == self.NIL:
        self.root = newNode
      elif newNode.data < y.data: 
        y.left = newNode
      else:
        y.right = newNode
    
      newNode.right = self.NIL
      newNode.left = self.NIL
    
      self.insert_fixup(newNode)
      
    
    def rb_transplant(self, x, y):
        
      RedBlackTree.comparing +=1 
      if x.parent == self.NIL:
        self.root = y
      elif x == x.parent.left:
        x.parent.left = y
      else:
        x.parent.right = y
      y.parent = x.parent
    
    def MinNode(self, x):
      while x.left != self.NIL:
        x = x.left
      return x
    
    def delete_fixup(self, x):
        
      while x != self.root and x.color == 0:
        RedBlackTree.comparing +=1 
        #Lewo pod drzewo
        if x == x.parent.left:
          w = x.parent.right
          #Wujek czerwony
          if w.color == 1:
            w.color = 0
            x.parent.color = 1
            self.left_rotate(x.parent)
            w = x.parent.right
            
          if w.left.color == 0 and w.right.color == 0:
            w.color = 1
            x = x.parent
    
          else:
            if w.right.color == 0:
              w.left.color = 0
              w.color = 1
              self.right_rotate(w)
              w = x.parent.right
    
            w.color = x.parent.color
            x.parent.color = 0
            w.right.color = 0
            self.left_rotate(x.parent)
            x = self.root
    
        else:
          w = x.parent.left
          if w.color == 1:
            w.color = 0
            x.parent.color = 1
            self.right_rotate(x.parent)
            w = x.parent.left
    
          if w.right.color == 0 and w.left.color == 0:
            w.color = 1
            x = x.parent
    
          else:
            if w.left.color == 0:
              w.right.color = 0
              w.color = 1
              self.left_rotate(w)
              w = x.parent.left
    
            w.color = x.parent.color
            x.parent.color = 0
            w.left.color = 0
            self.right_rotate(x.parent)
            x = self.root
    
      x.color = 0
      
    def pre_delete(self,node,value):
         RedBlackTree.size -=1
         self.Delete(node, value)
         
    def Delete(self,node ,value):
       
      tmp = self.getNode(node,value)
      if tmp == -1 : return
      y= tmp
      x = None
      y_orignal_color = y.color
      if tmp.left == self.NIL:
        x = tmp.right
        self.rb_transplant(tmp, tmp.right)
    
      elif tmp.right == self.NIL:
        x = tmp.left
        self.rb_transplant(tmp, tmp.left)
    
      else:
        y = self.MinNode(tmp.right)
        y_orignal_color = y.color
        x = y.right
        if y.parent == tmp:
          x.parent = tmp
    
        else:
          self.rb_transplant(y, y.right)
          y.right = tmp.right
          y.right.parent = y
    
        self.rb_transplant(tmp, y)
        y.left = tmp.left
        y.left.parent = y
        y.color = tmp.color
    
      if y_orignal_color == 0:
        self.delete_fixup(x)
    
    def getNode(self,node,value):
         RedBlackTree.comparing +=1 
         if node.data == value:
             return node
         RedBlackTree.comparing +=1 
         if node.left is not None:
            if node.data > value:
                return self.getNode(node.left,value)
         RedBlackTree.comparing +=1 
         if node.right is not None:
             if node.data <= value:
                 return self.getNode(node.right,value)
         else:
             return -1
         
    def Succesor(self,node,value):
        tmp = self.getNode(node,value)
        if tmp == -1:
            return -1
        if tmp.right is not None:
            return self.Min(tmp.right)
         
        y = node.parent
        while y != None and node == y.right:
            node = y
            y = y.parent
        if y == None:
            return -1
        return y
        
        
    def Find(self,node,value):
        RedBlackTree.comparing +=1 
        if node.data == value:
            return node.data
        RedBlackTree.comparing +=1 
        if node.left is not None:
            if node.data > value:
                return self.Find(node.left,value)
        RedBlackTree.comparing +=1  
        if node.right is not None:
            if node.data <= value:
                return self.Find(node.right,value)
            else:
                return -1
            
    def Inorder(self, n, value):
      if n != self.NIL:
        self.Inorder(n.left,value)
        value.append(n.data)
        self.Inorder(n.right,value)
      return value
  
    def Min(self,node):
        current = node
        while current.left is not None:
            if current.left.left == None:
                break
            current = current.left
        return current.data
    
    def Max(self,node):
        current = node
        while current.right is not None:
            if current.right.right == None:
                break 
            current = current.right
        return current.data


