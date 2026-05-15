class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        arr = sorted(set(nums))
        print(arr)
        ans = 0
        cur = 0
        for i in range(len(arr)):
            if i > 0 and arr[i] == arr[i-1] + 1:
                cur += 1 
            else:
                cur = 0
            ans = max(ans, cur)
        return ans + 1
        