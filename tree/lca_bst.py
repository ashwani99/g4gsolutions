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

        ptr = self.root
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
    
    def get_path_from_root(self, node_data):
        stack = []
        ptr = self.root
        while ptr:
            stack.append(ptr.data)
            if ptr.data > node_data:
                ptr = ptr.left
            elif ptr.data < node_data:
                ptr = ptr.right
            else:
                break
        
        return stack, len(stack)

    @staticmethod
    def LCA(root, node_data, other_node_data):
        while root:
            if node_data < root.data and other_node_data < root.data:
                root = root.left
            elif node_data > root.data and other_node_data > root.data:
                root = root.right
            else:
                return root.data

    @staticmethod
    def LCA_recursive(root, node_data, other_node_data):
        if root is None:
            return None

        if node_data < root.data and other_node_data < root.data:
            return BinarySearchTree.LCA_recursive(
                    root.left, node_data, other_node_data)
        elif node_data > root.data and other_node_data > root.data:
            return BinarySearchTree.LCA_recursive(
                    root.right, node_data, other_node_data)
        else:
            return root.data
    

if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.add_node(5)
    bst.add_node(3)
    bst.add_node(4)
    bst.add_node(2)
    bst.add_node(1)

    BinarySearchTree.inorder(bst.root)
    print(BinarySearchTree.LCA_recursive(bst.root, 1, 4))
    print(BinarySearchTree.LCA(bst.root, 1, 4))
