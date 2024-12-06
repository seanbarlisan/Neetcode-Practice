# Python program to demonstrate
# insert operation in binary search tree
class Node:
    def __init__(self, key):
        self.left = None # sets blueprint value for left side
        self.right = None # sets blueprint value for right side
        self.val = key # immediate set value for the key to have integer value


# A utility function to insert
# a new node with the given key
def insert(root, key):
    if root is None:
        return Node(key)
    if root.val == key: # if the value is equal to the key we want
            return root # return the node that we wish for 
    if root.val < key: # if it is left than key
            root.right = insert(root.right, key) # insert into the left of the key and continue searching recursively
    else:
            root.left = insert(root.left, key) # insert into the right of the key and continue searching recursively
    return root # the root exists already aka the node exists already


# A utility function to do inorder tree traversal
def inorder(root):
    if root:
        inorder(root.left) # recursively call inorder function to go into left side
        print(root.val, end=" ") # print whatever
        inorder(root.right) # repeat for rightside


# Creating the following BST
#      50
#     /  \
#    30   70
#   / \   / \
#  20 40 60 80
r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

# Print inorder traversal of the BST
inorder(r)