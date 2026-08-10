class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = {}
        res = []
        for x in nums:
            if n.get(x) != None:
                n[x] = n[x] + 1
            else:
                n[x] = 1
        for i in range(k):
            a = max(n, key = n.get)
            res.append(a)
            n.pop(a)
        return res



        