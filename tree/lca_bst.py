# https://practice.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-bst/1

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def add_node(self, data):
        newnode = Node(data)
        if not self.root:
            self.root = newnode
            return

        ptr = root
        ptr_parent = None
        while ptr:
            if ptr.data == data:
                return
            if ptr.data > data:
                parent = ptr
                ptr = ptr.left
            else:
                parent = ptr
                ptr = ptr.right

        if parent.data > data:
            parent.left = newnode
        else:
            parent.right = newnode

    @staticmethod
    def inorder(root):
        if root:
            BinarySearchTree.inorder(root.left)
            print(root.data)
            BinarySearchTree.inorder(root.right)

    @staticmethod
    def LCS(node, other_node):
        pass
