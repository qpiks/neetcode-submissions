class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = {}
        
        for i in range(len(nums)):
            if n.get(target - nums[i]) != None:
                return [n[target - nums[i]], i]
            n.update({nums[i]: i})
        return n
                
            
            

        

        