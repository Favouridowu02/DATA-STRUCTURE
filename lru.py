from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        
        self.cache[key] = value
        
        # Check capacity
        if len(self.cache) > self.capacity:
            # popitem(last=False) removes the FIRST item (FIFO/Least Recently Used)
            self.cache.popitem(last=False)


obj = LRUCache(5)
param_1 = obj.get(1)
print(param_1)
obj.put(1, 5)
obj.put(2, 4)
obj.put(3, 3)
obj.put(4, 2)
obj.put(5, 1)

print(obj.get(2))
print(obj.get(10))
print(obj.get(5))
print(obj.get(3))
print(obj.get(1))
print(obj.get(2))
print(obj.get(4))
print(obj.cache)