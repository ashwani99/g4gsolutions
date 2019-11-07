# https://practice.geeksforgeeks.org/problems/height-of-binary-tree/1

def get_height(root):
    if root is None:
        return -1
    return max(get_height(root.left), get_height(root.right))+1


from bottom_view import BinaryTree

if __name__ == '__main__':
    bt = BinaryTree()
    bt.add_node(1)
    bt.add_node(2)
    bt.add_node(3)
    bt.add_node(4)
    print('Height', get_height(bt.root))

