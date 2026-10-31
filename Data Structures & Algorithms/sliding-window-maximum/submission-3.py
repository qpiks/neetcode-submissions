import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = deque()
        l, r = 0, 0

        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if (r + 1 >= k):
                ans.append(nums[q[0]])
                l += 1
        return ans
        
        
        # # heap:
        # window = []
        # ans = []
        # seen = {}
        # for i in range(k):
        #     n = nums[i]
        #     heapq.heappush(window, -n)
        #     seen[n] = seen.get(n, 0) + 1
        # ans.append(-window[0])
        # for i in range(k, len(nums)):
        #     n = nums[i]
        #     heapq.heappush(window, -n)
        #     seen[n] = seen.get(n, 0) + 1
        #     seen[nums[i - k]] -= 1
        #     while seen[-window[0]] <= 0: 
        #         heapq.heappop(window)
        #     ans.append(-window[0])
        # return ans
            



        