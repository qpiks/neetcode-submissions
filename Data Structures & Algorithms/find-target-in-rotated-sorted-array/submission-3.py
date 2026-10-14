class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            # print(l, m, r)
            if nums[m] == target: 
                return m
            if nums[l] <= nums[m]:
                # print("huh")
                if target < nums[m] and target >= nums[l]:
                    r = m - 1
                    # print("huh1")
                else:
                    l = m + 1
                    # print("huh2")
            else: #l non conseq
                if target >= nums[l] or target < nums[m]:
                    r = m - 1
                else: 
                    l = m + 1







            # if nums[l] < target and target < nums[m]:
            #     r = m - 1
            # elif nums[m] < target and target < nums[r]:
            #     l = m + 1
            
            # elif nums[m] > target and nums[r] > target: ???
            #     l = m + 1

            # elif target < num[l] and target < num[m]:
            #     l = m + 1
                
                


        return -1
        