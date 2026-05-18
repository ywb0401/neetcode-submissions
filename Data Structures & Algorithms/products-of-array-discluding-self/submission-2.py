class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        leftfix = 1
        for i in range(len(nums)):
            res.append(leftfix)
            leftfix *= nums[i] 
        
        rightfix = 1
        for j in range(len(nums)-1, -1, -1):
            res[j] *= rightfix
            rightfix *= nums[j] 
        return res