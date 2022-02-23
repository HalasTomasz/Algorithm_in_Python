class Nodes:
    
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

class SplayTree:
       
    comparing = 0
    size = 0
    Msize = 0

    def __init__(self):
        self.root = None

    def maxi(self, x):
        while x.right != None:
            x = x.right
        return x

    def mini(self, x):
        while x.left != None:
            x = x.left
        return x

    def Max(self):
        tmp = self.root
        while tmp.right != None:
            tmp = tmp.right
        return tmp.data

    def Min(self):
        tmp = self.root
        while tmp.left != None:
            tmp = tmp.left
        return tmp.data

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None: 
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
        if y.right != None:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None: 
            self.root = y

        elif x == x.parent.right:
            x.parent.right = y

        else: 
            x.parent.left = y

        y.right = x
        x.parent = y

    def splay(self, node):
        while node.parent != None:  
            if node.parent == self.root:  
                if node == node.parent.left:
                    self.right_rotate(node.parent)
                else:
                    self.left_rotate(node.parent)

            else:
                x = node.parent #rodzic
                y = x.parent #dziadek 
                #Zig
                if node.parent.left == node and x.parent.left == x:  
                    self.right_rotate(y)
                    self.right_rotate(x)
                #Zig Zig
                elif node.parent.right == node and x.parent.right == x: 
                    self.left_rotate(y)
                    self.left_rotate(x)
                #Zig zag
                elif node.parent.right == node and x.parent.left == x:
                    self.left_rotate(x)
                    self.right_rotate(y)
                #odbicie lustrzane
                elif node.parent.left == node and x.parent.right == x:
                    self.right_rotate(x)
                    self.left_rotate(y)

    def pre_insert(self,value):
         SplayTree.size +=1
         if SplayTree.size > SplayTree.Msize:
            SplayTree.Msize = SplayTree.size 
         self.Insert(value)
        
    def Insert(self, key):
        
        y = None
        node = Nodes(key)
        temp = self.root
        while temp != None:
            y = temp
            SplayTree.comparing += 1
            if node.data < temp.data:
                temp = temp.left
            else:
                temp = temp.right

        node.parent = y
        if y == None:  
            self.root = node
        elif node.data < y.data:
            SplayTree.comparing += 1
            y.left = node
        else:
            SplayTree.comparing += 1
            y.right = node

        self.splay(node)

    def Search(self, node, val):
        
        if node is None:
            return node
        
        SplayTree.comparing += 1
        if val == node.data:
            #self.splay(node)
            return node
        
        elif val < node.data:
            SplayTree.comparing += 1
            return self.Search(node.left, val)
        else:
            SplayTree.comparing += 2
            return self.Search(node.right, val)


    def Find(self, node, val):
        
        if node is None:
            return 0
        
        SplayTree.comparing += 1
        if val == node.data:
            self.splay(node)
            return 1

        elif val < node.data:
            SplayTree.comparing += 1
            return self.Find(node.left, val)
        
        elif val >= node.data:
            SplayTree.comparing += 2
            return self.Find(node.right, val)
        
        else:
            SplayTree.comparing += 2
            return 0

    def pre_delete(self,node,value):
         SplayTree.size -=1
         self.Delete(node, value)
         
    def Delete(self,node, key):
        x = self.Search(node,key)
        
        if x:
            self.splay(x)

            left_subtree = SplayTree()
            left_subtree.root = self.root.left
            if left_subtree.root != None:
                left_subtree.root.parent = None

            right_subtree = SplayTree()
            right_subtree.root = self.root.right
            if right_subtree.root != None:
                right_subtree.root.parent = None

            if left_subtree.root != None:
                m = left_subtree.maxi(left_subtree.root)
                left_subtree.splay(m)
                left_subtree.root.right = right_subtree.root
                self.root = left_subtree.root

            else:
                self.root = right_subtree.root
                
    def Inorder(self, node, val):
        if node != None:
            self.Inorder(node.left,val)
            val.append(node.data)
            self.Inorder(node.right,val)
        return val

    def Succesor(self, key):
        
        if self == None:
            return -1

        node = self.Search(self.root,key)

        if node == None:
            return -1

        if node.right != None:
            return self.mini(node.right).data
        
        y = node.parent
        while y != None and node == y.right:
            node = y
            y = y.parent
            
        if y == None:
            return -1
        return y
        