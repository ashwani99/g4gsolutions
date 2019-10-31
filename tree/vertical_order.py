# https://practice.geeksforgeeks.org/problems/print-a-binary-tree-in-vertical-order/1

from bottom_view import BinaryTree

def vertical_order_util(root, vertical_dict, side_level=0):
    if root is None:
        return
    if side_level not in vertical_dict:
        vertical_dict[side_level] = [root.data]
    else:
        vertical_dict[side_level].append(root.data)
    vertical_order_util(root.left, vertical_dict, side_level-1)
    vertical_order_util(root.right, vertical_dict, side_level+1)


def print_in_vertical_order(tree):
    vertical_dict = {}
    vertical_order_util(tree.root, vertical_dict)

    for _, nodes in sorted(vertical_dict.items()):
        for node in nodes:
            print(node, end=' ')
    print()


if __name__ == '__main__':
    bt = BinaryTree()
    bt.add_node(1)
    bt.add_node(2)
    bt.add_node(3)
    bt.add_node(4)
    bt.add_node(5)
    bt.add_node(6)
    bt.add_node(7)
    bt.add_node(8)
    bt.add_node(9)
    bt.add_node(0)
    print_in_vertical_order(bt)

