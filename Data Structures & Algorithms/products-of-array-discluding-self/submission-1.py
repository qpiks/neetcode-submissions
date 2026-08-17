class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mlt = 1
        zero = 0
        res = nums
        for i in range(len(nums)):
            if nums[i] != 0:
                mlt *= nums[i]
            else: 
                zero += 1
        for i in range (len(nums)): 
            if zero > 0:
                if res[i] == 0 and zero == 1:
                    res[i] = mlt
                else: 
                    res[i] = 0

            else:
                res[i] = mlt // res[i]
        return res
        




        