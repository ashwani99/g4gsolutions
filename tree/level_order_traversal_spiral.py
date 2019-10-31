# https://practice.geeksforgeeks.org/problems/level-order-traversal-in-spiral-form/1

from bottom_view import BinaryTree

def level_order(root, level_order_dict, level=0):
    if root is None:
        return

    if level in level_order_dict:
        level_order_dict[level].append(root.data)
    else:
        level_order_dict[level] = [root.data]

    level_order(root.left, level_order_dict, level+1)
    level_order(root.right, level_order_dict, level+1)


def level_order_spiral(tree):
    level_order_dict = {}
    level_order(tree.root, level_order_dict)

    reverseToggle = False
    for _, nodes in sorted(level_order_dict.items()):
        if not reverseToggle:
            for node in nodes[::-1]:
                print(node, end=' ')
        else:
            for node in nodes:
                print(node, end=' ')
        reverseToggle = not reverseToggle
    print()


if __name__ == '__main__':
    bt = BinaryTree()
    bt.add_node(1)
    bt.add_node(2)
    bt.add_node(3)
    bt.add_node(4)
    bt.add_node(5)
    bt.add_node(6)
    level_order_spiral(bt)

    bt.clear()
    bt.add_node(10)
    bt.add_node(20)
    bt.add_node(30)
    bt.add_node(40)
    bt.add_node(60)
    level_order_spiral(bt)
