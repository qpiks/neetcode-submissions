class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:    
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            p1, p2, p3 = i, i + 1, len(nums) - 1
            while p1 < p2 and p2 < p3:
                curr = nums[p1] + nums[p2] + nums[p3]
                if curr == 0:
                    res.append([nums[p1], nums[p2], nums[p3]])
                    p2 += 1
                    p3 -= 1
                    print((p2))
                    while p2 < p3 and nums[p2] == nums[p2 - 1]:
                        p2 += 1
                        print(p2)
                elif curr > 0:
                    p3 -=  1
                else:
                    p2 += 1

        return res



        
        