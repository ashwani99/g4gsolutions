# https://practice.geeksforgeeks.org/problems/maximum-path-sum/1

from bottom_view import BinaryTree, Node

def max_path_sum(root):
    if not root:
        return 0
    mps_left = max_path_sum(root.left)
    mps_right = max_path_sum(root.right)

    mps_single = max(max(mps_left, mps_right) + root.data, root.data)

    max_path_sum.res = max(mps_single, mps_left + mps_right + root.data)

    return mps_single


if __name__ == '__main__':
    bt = BinaryTree()
    bt.add_node(10)
    bt.root.left = Node(2)
    bt.root.right = Node(10)
    bt.root.left.left = Node(20)
    bt.root.left.right = Node(1)
    bt.root.right.right = Node(-25)
    bt.root.right.right.left = Node(3)
    bt.root.right.right.right = Node(4)

    max_path_sum.res = float("-inf")
    max_path_sum(bt.root)
    print(max_path_sum.res)

