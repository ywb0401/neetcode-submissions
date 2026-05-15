class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = 1
        ans = [1] * n
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]

        rightfix = 1
        for j in range(n-1, -1, -1):
            ans[j] *= rightfix
            rightfix *= nums[j]
            
        return ans

