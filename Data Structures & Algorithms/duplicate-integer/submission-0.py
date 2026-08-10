class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}

        for x in nums:
            if count.get(x):
                return True
            else:
                count.update({x:1})
        return False

        