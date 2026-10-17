class TimeMap:

    def __init__(self):
        self.hashmap = {}         

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.hashmap.get(key, 0) == 0:
            self.hashmap[key] = []
        self.hashmap[key].append(tuple([timestamp, value]))            
        

    def get(self, key: str, timestamp: int) -> str:
        array = self.hashmap.get(key, [])
        if not array:
            return ""
        l, r = 0, len(array) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if array[m][0] == timestamp: 
                return array[m][1]
            if array[m][0] > timestamp:
                if (m - 1) >= 0 and array[m - 1][0] < timestamp:
                    return array[m - 1][1]
                r = m - 1
            else:
                if (m + 1) >= len(array) or array[m + 1][0] > timestamp:
                    return array[m][1]
                l = m + 1
        return ""
        
