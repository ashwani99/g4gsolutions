# https://practice.geeksforgeeks.org/problems/check-for-bst/1

from left_view import BinaryTree, Node

INT_MIN = -10**10
INT_MAX = 10**10


class BT(BinaryTree):
    @staticmethod
    def is_bst(root, mini=INT_MIN, maxi=INT_MAX):
        if root:
            if root.data < mini or root.data > maxi:
                return False
            return BT.is_bst(root.left, mini, root.data-1) and BT.is_bst(root.right, root.data+1, maxi)
        return True

    def clear(self):
        self.root = None


if __name__ == '__main__':
    bst = BT()
    
    bst.add_node(1)
    bst.add_node(2)
    bst.add_node(3)
    bst.add_node(4)
    bst.add_node(5)
    bst.add_node(6)
    bst.add_node(7)
    bst.add_node(8)
    bst.add_node(9)
    bst.add_node(10)
    bst.add_node(11)
    print(BT.is_bst(bst.root))

    bst.clear()
    bst.add_node(4)
    bst.add_node(2)
    bst.add_node(5)
    bst.add_node(1)
    bst.add_node(3)
    print(BT.is_bst(bst.root))

    bst.clear()
    bst.add_node(10)
    bst.add_node(20)
    bst.add_node(30)
    bst.add_node(40)
    bst.add_node(60)
    print(BT.is_bst(bst.root))

    bst.clear()
    bst.root = Node(20)
    bst.root.left = Node(10)
    bst.root.right = Node(30)
    bst.root.left.left = Node(5)
    bst.root.left.left.left = Node(2)
    bst.root.left.left.left.right = Node(3)
    bst.root.right.left = Node(15)
    print(BT.is_bst(bst.root, INT_MIN, INT_MAX))
