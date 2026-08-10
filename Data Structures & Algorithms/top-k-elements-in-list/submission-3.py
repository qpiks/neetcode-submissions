class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = {}
        arr = []
        for x in nums:
            if n.get(x) != None:
                n[x] = n[x] + 1
            else:
                n[x] = 1
        for i in n:
            arr.append([n[i], i])
        arr.sort()
        res = []
        for i in range(k):
            res.append(arr[len(arr) - i - 1][1])
        return res



        