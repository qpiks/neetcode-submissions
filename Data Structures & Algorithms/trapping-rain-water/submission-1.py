class Solution:
    def trap(self, height: List[int]) -> int:
        amount = 0
        m = 0
        l = []
        r = [None] * len(height)
        for i in range(len(height)):
            if height[i] > m:
                m = height[i]
            l.append(m)
        m = 0
        
        for i in range(len(height) - 1, -1, -1):
            if height[i] > m:
                m = height[i]
            r[i] = m
        # print(l)
        # print(r)
        for i in range(1, len(height) - 1):
            if (min(l[i], r[i]) - height[i]) > 0:
                amount += min(l[i], r[i]) - height[i]
            # print(amount, l[i], r[i], height[i], i)

        return amount



        