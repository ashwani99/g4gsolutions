# https://practice.geeksforgeeks.org/problems/serialize-and-deserialize-a-binary-tree/1

from collections import deque
from bottom_view import BinaryTree, Node

def serialize(root, arr):
    if root is None:
        return None

    q = deque([root])
    arr.append(root)
    while q:
        popped = q.popleft()
        if popped:
            q.append(popped.left)
            arr.append(popped.left)
            q.append(popped.right)
            arr.append(popped.right)


def deserialize(arr):
    ptr = root = None
    index = 0
    q = deque()
    while index < len(arr):
        if root is None:
            root = arr[index]
            index += 1
            q.append(root)
        else:
            while q[0] is None:
                q.popleft()
            # print('Queue:', q)
            ptr = q[0]
            # print('Here', ptr, arr[index:])
            ptr.left = arr[index]
            ptr.right = arr[index+1]
            q.popleft()
            q.append(ptr.left)
            q.append(ptr.right)
            index += 2

    return root



def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.data)
        print_inorder(root.right)


if __name__ == '__main__':
    bt = BinaryTree()
    bt.add_node(1)
    bt.add_node(2)
    bt.add_node(3)
    bt.add_node(4)
    bt.add_node(5)
    bt.add_node(6)
    bt.add_node(7)

    print_inorder(bt.root)

    arr = []
    serialize(bt.root, arr)
    # print(arr)
    
    bt_new = deserialize(arr)
    print_inorder(bt_new)
