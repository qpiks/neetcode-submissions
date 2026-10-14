class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            print(l, r)
            if nums[l] <= nums[r]:
                return nums[l]
            m = l + ((r - l) // 2)
            print(m)
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                l = l + 1
                r = m

        return nums[0]