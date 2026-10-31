import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # ans = []
        # seen = {}
        # maximum = nums[0]
        # for i in range(k):
        #     n = nums[i]
        #     seen[n] = seen.get(n, 0) + 1
        #     if n > maximum:
        #     maximum = n
        # ans.append(maximum)

        # for i in range(1, len(nums) - k + 1):
        #     seen[i - 1] -=1

        window = []
        ans = []
        seen = {}
        for i in range(k):
            n = nums[i]
            heapq.heappush(window, -n)
            seen[n] = seen.get(n, 0) + 1
        ans.append(-window[0])
        for i in range(k, len(nums)):
            n = nums[i]
            heapq.heappush(window, -n)
            seen[n] = seen.get(n, 0) + 1
            seen[nums[i - k]] -= 1
            while seen[-window[0]] <= 0: 
                heapq.heappop(window)
            ans.append(-window[0])
        return ans
            



        