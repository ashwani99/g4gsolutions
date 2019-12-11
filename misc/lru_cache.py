from collections import deque


class LRUCache:
    def __init__(self, max_size):
        self.max_size = max_size
        self.map = {}
        self.keys = deque()

    def get(self, key):
        if key not in self.map:
            return -1
        value = self.map.get(key)
        self.keys.remove(key)
        self.keys.appendleft(key)
        return value

    def insert(self, key, value):
        if key in self.map:
            self.keys.remove(key)

        self.map[key] = value

        if len(self.map.keys()) > self.max_size:
            k = self.keys.pop()
            del self.map[k]
        self.keys.appendleft(key)
        

t = int(input())
for _ in range(t):
    n = int(input())
    lru = LRUCache(n)
    q = int(input())
    inputs = input().split()

    # print(inputs)
    while q > 0:
        # print('MAP IS: ', lru.map)
        # print('QUEUE IS: ', lru.keys)
        if inputs[0] == 'SET':
            # print(inputs[0:3])
            lru.insert(int(inputs[1]), int(inputs[2]))
            inputs.pop(0)
            inputs.pop(0)
            inputs.pop(0)
        elif inputs[0] == 'GET':
            # print(inputs[0:2])
            print(lru.get(int(inputs[1])), end=' ')
            inputs.pop(0)
            inputs.pop(0)
        q = q - 1
    print()
