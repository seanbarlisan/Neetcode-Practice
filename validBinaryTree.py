class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left

def validTree(self, root): 
    if not root:
        return True


if __name__ == "__main__":
    tree = [2, 1, 3]
    n = validTree(tree)
    print(n)