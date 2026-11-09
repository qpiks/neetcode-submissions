class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        

    def get(self, key: int) -> int:
        ans = self.cache.get(key, -1)
        if ans != -1:
            del self.cache[key]
            self.cache[key] = ans
        return ans

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
        elif len(self.cache) == self.capacity:
            del self.cache[list(self.cache)[0]]
        self.cache[key] = value

        
