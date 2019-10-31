# https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1

from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

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


    def print_left_view(self):
        left_view = []
        q = deque([self.root, None])
        is_new_level = True
        while q:
            # print(q)
            popped = q.popleft()
            if popped is None:
                break

            if is_new_level:
                left_view.append(popped)
                is_new_level = False

            if q[0] is None:
                q.popleft()
                is_new_level = True
            
            if popped.left:
                q.append(popped.left)
            if popped.right:
                q.append(popped.right)

            if is_new_level:
                q.append(None)


        for node in left_view:
            print(node.data, end=' ')
        print()


    def left_view_recursive(self):
        left_view_dict = {}
        self._left_view_util(self.root, 0, left_view_dict)
        for key in left_view_dict:
            print(left_view_dict[key], end=' ')
        print()


    def _left_view_util(self, root, level, left_view_dict):
        if root:
            if level not in left_view_dict:
                left_view_dict[level] = root.data

            self._left_view_util(root.left, level+1, left_view_dict)
            self._left_view_util(root.right, level+1, left_view_dict)

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
    bt.print_left_view()
    bt.left_view_recursive()
