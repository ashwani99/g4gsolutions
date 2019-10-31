# https://practice.geeksforgeeks.org/problems/connect-nodes-at-same-level/1

from bottom_view import BinaryTree

def level_order(root, level_order_map, level=0):
    if root is None:
        return

    if level not in level_order_map:
        level_order_map[level] = [root]
    else:
        level_order_map[level].append(root)

    level_order(root.left, level_order_map, level+1)
    level_order(root.right, level_order_map, level+1)


def connect_nodes(level_order_map):
    for _, nodes in level_order_map.items():
        for i in range(1, len(nodes)):
            nodes[i-1].nextRight = nodes[i]
        nodes[-1].nextRight = None


if __name__ == '__main__':
    bt = BinaryTree()
    bt.add_node(10)
    bt.add_node(3)
    bt.add_node(5)
    bt.add_node(4)
    bt.add_node(1)
    bt.add_node(2)

    level_order_map = {}
    level_order(bt.root, level_order_map)
    connect_nodes(level_order_map)

    print('These nodes are connected')
    for level in level_order_map:
        ptr = level_order_map[level][0]
        while ptr:
            print(ptr.data, end='-->')
            ptr = ptr.nextRight
        print()
