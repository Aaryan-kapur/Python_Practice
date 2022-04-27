class node:
  def __init__(self,key):
    self.left =  None
    self.right =  None
    self.val = key

def printinorder(r):
  if r:
    printinorder(r.left)
    print(r.val)
    printinorder(r.right)
def printpreorder(r):
  if r:
    print(r.val)
    printpreorder(r.left)
    printpreorder(r.right)
def printpostorder(r):
  if r:
    printpostorder(r.left)
    printpostorder(r.right)
    print(r.val)


root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)


printpostorder(root)
