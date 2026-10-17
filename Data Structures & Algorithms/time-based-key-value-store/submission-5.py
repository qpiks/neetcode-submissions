class TimeMap:

    def __init__(self):
        self.hashmap = {}         

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.hashmap.get(key, 0) == 0:
            self.hashmap[key] = []
        self.hashmap[key].append([timestamp, value])            
        

    def get(self, key: str, timestamp: int) -> str:
        array = self.hashmap.get(key, [])
        ans = ""
        l, r = 0, len(array) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if array[m][0] <= timestamp: 
                ans = array[m][1]
                l = m + 1
            else:
                r = m - 1
        return ans
        
