class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid

            # Check if the left half is sorted
            if nums[l] <= nums[mid]:
                # Check if target lies within the sorted left half
                if nums[l] <= target < nums[mid]:
                    r = mid - 1  # Search left
                else:
                    l = mid + 1
            else:
                # Check if target lies within the sorted right half
                if nums[mid] < target <= nums[r]:
                    l = mid + 1  # Search right
                else:
                    r = mid - 1

        return -1
        # l, r = 0, len(nums) - 1
        # while l <= r:
        #     m = l + ((r - l) // 2)
        #     if nums[m] == target: 
        #         return m
        #     if nums[l] <= nums[m]:
        #         if target < nums[m] and target >= nums[l]:
        #             r = m - 1
        #         else:
        #             l = m + 1
        #     else:
        #         if target >= nums[l] or target < nums[m]:
        #             r = m - 1
        #         else: 
        #             l = m + 1
        # return -1