import BSTree
import argparse
import sys
import RBTree
def load(file_Name,Tree):
    
    try:
        Data = open(file_Name,'r')
        for line in Data:
            Tree.insert(line.strip('\n'))
            
    except OSError:
        print ("Could not open/read file: "+ str(file_Name))

def Job(Orders, Tree):
    
    if Orders[0] == 'insert':
        Tree.insert(Orders[1])
    elif Orders[0] == 'delete':
        Tree.delete(Orders[1])
    elif Orders[0] == 'max':
        sys.stdout.write(str(Tree.max()) + '\n')
    elif Orders[0] == 'min':
        sys.stdout.write(str(Tree.min()))
    elif Orders[0] == 'find':
        sys.stdout.write(str(Tree.find(Orders[1])) +'\n' )
    elif Orders[0] == 'inorder':
        sys.stdout.write(str(Tree.inorder([]))+'\n')
    elif Orders[0] == 'load':
        load(Orders[1],Tree)
    elif Orders[0] =='successor':
         tmp=Tree.successor(Orders[1])
         if tmp == -1:
              sys.stdout.write('\n')
         else:
              sys.stdout.write(str(Orders[1])+'\n')
    else:
        sys.stdout.write("Unkown Command :" + str(Orders[0]))
        
if __name__ == '__main__':
    
  parser = argparse.ArgumentParser()
  parser.add_argument('--type', action="store", type=str)
  args = parser.parse_args()
  tree_Type = args.type
  
  if tree_Type == 'bst':
      Tree = BSTree.BSTNode()
  elif tree_Type == 'rbt':
      Tree =  RBTree.RedBlackTree()
  else:
      pass
  #IF ELSE WHETHER TREE IS USED
  given = sys.stdin.read().splitlines()
  for line in given:
      tmp = line.split(" ")
      Job(tmp,Tree)
      
