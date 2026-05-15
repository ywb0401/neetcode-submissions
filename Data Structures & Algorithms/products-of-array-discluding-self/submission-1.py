class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        leftfix = 1
        for i in range(n):
            ans[i] = leftfix
            leftfix *= nums[i]
        
        rightfix = 1
        for j in range(n-1, -1, -1):
            ans[j] *= rightfix
            rightfix *= nums[j]
        
        return ans
    
