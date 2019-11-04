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

    def LCS(self, node, other_node):
        path1, count1 = self.get_path_from_root(node)
        path2, count2 = self.get_path_from_root(other_node)
        
        if count1 == 0 or count2 == 0:
            print('Not able to find nodes')
            return

        while count1 != count2:
            if count1 > count2:
                path1.pop()
                count1 -= 1
            else:
                path2.pop()
                count2 -= 1

        while path1[-1] != path2[-1]:
            path1.pop()
            path2.pop()

        return path1[-1]
    

if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.add_node(5)
    bst.add_node(3)
    bst.add_node(4)
    bst.add_node(2)
    bst.add_node(1)

    BinarySearchTree.inorder(bst.root)
    print(bst.LCS(1, 4))
