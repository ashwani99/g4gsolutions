class Heap:
    def __init__(self, items=[]):
        if not isinstance(items, list):
            raise TypeError('Heap items should be a list')
        self._items = items

    def add_node(self, data):
        self._items.append(data)

    def parent_index(self, index):
        return index//2

    def left_child_index(self, parent_index):
        return 2*parent_index + 1
    
    def right_child_index(self, parent_index):
        return 2*parent_index + 2

    def max_heapify(self, i):
        left = self.left_child_index(i)
        right = self.right_child_index(i)
        # getting the largest element's index
        if left < len(self._items) and self._items[left] > self._items[i]:
            largest = left
        else:
            largest = i
        if right < len(self._items) and self._items[right] > self._items[largest]:
            largest = right
        
        self._items[largest], self._items[i] = self._items[i], self._items[largest]
        if largest != i:
            self.max_heapify(largest)

    def min_heapify(self, i):
        left = self.left_child_index(i)
        right = self.right_child_index(i)

        if left < len(self._items) and self._items[left] < self._items[i]:
            smallest = left
        else:
            smallest = i
        if right < len(self._items) and self._items[right] < self._items[smallest]:
            smallest = right

        self._items[smallest], self._items[i] = self._items[i], self._items[smallest]
        if smallest != i:
            self.min_heapify(smallest)

    def build_max_heap(self):
        n = len(self._items)
        for i in range(n//2, -1, -1):
            self.max_heapify(i)

    def build_min_heap(self):
        n = len(self._items)
        for i in range(n//2, -1, -1):
            self.min_heapify(i)
    
    def heapsort(self, order='asc'):
        if order == 'asc':
            self.build_max_heap()
        else:
            self.build_min_heap()
        
        sorted_list = []
        last_index = len(self._items)-1
        for i in range(last_index):
            self._items[i], self._items[0] = self._items[i], self._items[0]

    def print_heap(self):
        print(' '.join(map(lambda x: str(x), self._items)))


if __name__ == '__main__':
    my_list = [7, 8, 14, 10, 9, 3, 16, 1, 4, 2]
    h = Heap(my_list)
    h.print_heap()

    #h.build_max_heap()
    print('Max Heap')
    h.print_heap()

    print('Min heap')
    #h.build_min_heap()
    h.print_heap()
    
    h.heapsort()
    h.print_heap()
