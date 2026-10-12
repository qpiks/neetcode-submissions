class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = r
        while l <= r:
            m = l + ((r - l) // 2)
            print(m)
            hours = 0
            for i in range(len(piles)):
                hours += (piles[i] + m - 1) // m
            if hours <= h:
                r = m - 1
                if m < ans:
                    ans = m
                else: 
                    l = m + 1
            elif hours > h:
                l = m + 1
        return ans
            
            