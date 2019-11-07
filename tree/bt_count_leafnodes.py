# https://practice.geeksforgeeks.org/problems/count-leaves-in-binary-tree/1

from bottom_view import BinaryTree

def count_leaf_nodes(root):
    if root is None:
        return 0
    if not root.left and not root.right:
        return 1
    return count_leaf_nodes(root.left) +\
           count_leaf_nodes(root.right)


if __name__ == '__main__':
    bt = BinaryTree()
    bt.add_node(1)
    bt.add_node(2)
    bt.add_node(3)
    bt.add_node(4)
    print(count_leaf_nodes(bt.root))

