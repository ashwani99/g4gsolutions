# https://practice.geeksforgeeks.org/problems/check-for-balanced-tree/1

from bottom_view import BinaryTree, Node

def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right))+1

def isBalanced(root):
    if root is None:
        return True
    lheight = height(root.left)
    rheight = height(root.right)
    
    if abs(lheight-rheight) > 1:
        return False
    return isBalanced(root.left) and isBalanced(root.right)


if __name__ == '__main__':
    bt = BinaryTree()
    bt.add_node(1)
    bt.root.
