from collections import deque

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def clear(self):
        self.root = None

    # this adds the nodes in level order of the tree
    def add_node(self, data):
        newnode = Node(data)
        if self.root is None:
            self.root = newnode
            return

        q = deque([self.root])
        while q:
            popped = q.popleft()
            if popped.left:
                q.append(popped.left)
            else:
                popped.left = newnode
                return
            if popped.right:
                q.append(popped.right)
            else:
                popped.right = newnode
                return

    @staticmethod
    def bottom_view(root, bottom_view_dict, side_level=0):
        if not root:
            return
        bottom_view_dict[side_level] = root.data
        
        BinaryTree.bottom_view(root.left, bottom_view_dict, side_level-1)
        BinaryTree.bottom_view(root.right, bottom_view_dict, side_level+1)


def print_bottom_view(tree):
    bv_dict = {}
    BinaryTree.bottom_view(tree.root, bv_dict)
    
    for level, data in sorted(bv_dict.items()):
        print(data, end=' ')
    print()


if __name__ == '__main__':
    bt = BinaryTree()
    
    bt.add_node(10)
    bt.add_node(20)
    bt.add_node(30)
    bt.add_node(40)
    bt.add_node(60)
    print_bottom_view(bt)

    bt.clear()
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
    print_bottom_view(bt)

