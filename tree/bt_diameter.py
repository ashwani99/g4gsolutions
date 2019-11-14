# https://practice.geeksforgeeks.org/problems/diameter-of-binary-tree/1

from bottom_view import BinaryTree


def get_height(root):
    if not root:
        return 0
    return max(get_height(root.left), get_height(root.right)) + 1


def get_diameter(root):
    if not root:
        return 0
    return max(get_diameter(root.left),
               get_diameter(root.right),
               get_height(root.left)+get_height(root.right)+1)


if __name__ == '__main__':
    bt = BinaryTree()
    bt.add_node(1)
    bt.add_node(2)
    bt.add_node(3)
    bt.add_node(4)
    bt.add_node(5)
    print(get_diameter(bt.root))
