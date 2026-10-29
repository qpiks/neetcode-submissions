from collections import deque
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        minimum = prices[0]
        for i in range(len(prices)):
            ans = max(prices[i] - minimum, ans)
            minimum = min(minimum, prices[i])
    

        return ans
        


        